#!/usr/bin/env python3
"""CAD package for a combined set (Shane 2026-10-11 7:20 PM CT): sheet DXFs as drawn (sheet inches) + plan DXFs re-scaled to real feet
(model space, origin = building / room grid 0,0) + optional OBJ / MTL + README_CAD.txt, zipped deterministically (fixed dates, sorted).

  python blueprints/shared/cad_package.py phase2|phase2g|phase1|phase1mb      (run from the repo root; writes phase*/out/pdf/THA_Phase*_CAD_Rev*.zip)
"""
import io
import os
import re
import sys
import tempfile
import zipfile

import ezdxf
from ezdxf.math import Matrix44

BP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
P2, P1 = os.path.join(BP, "phase2", "out"), os.path.join(BP, "phase1", "out")

SETS = {
    "phase2": dict(
        zip="THA_Phase2_CAD_RevF.zip", set_name="Phase 2 Schematic Set Rev F (index = P2-G-001 Rev E)",
        sheets=["P2-G-001_RevE", "P2-G-002_RevG", "P2-G-003_RevN", "P2-C-101_RevH", "P2-A-101_RevN", "P2-A-102_RevI", "P2-A-103_RevE",
                "P2-A-111_RevF", "P2-A-201_RevM", "P2-A-301_RevF", "P2-A-302_RevC", "P2-A-401_RevE", "P2-A-901_RevH"],
        dxf_dir=os.path.join(P2, "dxf"),
        # plan -> feet: (sheet, ox, oy, in-per-ft, window ft). Origins from the generators (p2_a_101_rev_n.py / p2_a_102_rev_i.py OX, OY = 1.05,
        # top + 0.55 = 2.90; p2_a_111_rev_f.py 1.15, top + 1.05 = 3.40, L1 plan only), checked on the 30 ft drum circle at (182, 262.5).
        feet=[("P2-A-101_RevN", 1.05, 2.90, 1 / 40, (-70, -90, 330, 345)), ("P2-A-102_RevI", 1.05, 2.90, 1 / 40, (-70, -90, 330, 345)),
              ("P2-A-111_RevF", 1.15, 3.40, 1 / 40, (-70, -90, 330, 345))],
        model=[os.path.join(P2, "3d", "P2-A-901_RevH_massing.obj"), os.path.join(P2, "3d", "P2-A-901_RevH_massing.mtl")],
        extra=[]),
    "phase2g": dict(
        zip="THA_Phase2_CAD_RevG.zip", set_name="Phase 2 Schematic Set Rev G (index = P2-G-001 Rev F; D-091 solar CUT, D-092, D-093)",
        sheets=["P2-G-001_RevF", "P2-G-002_RevG", "P2-G-003_RevN", "P2-C-101_RevH", "P2-A-101_RevN", "P2-A-102_RevI", "P2-A-103_RevE",
                "P2-A-111_RevF", "P2-A-201_RevN", "P2-A-301_RevF", "P2-A-302_RevC", "P2-A-401_RevE", "P2-A-901_RevI"],
        dxf_dir=os.path.join(P2, "dxf"),
        feet=[("P2-A-101_RevN", 1.05, 2.90, 1 / 40, (-70, -90, 330, 345)), ("P2-A-102_RevI", 1.05, 2.90, 1 / 40, (-70, -90, 330, 345)),
              ("P2-A-111_RevF", 1.15, 3.40, 1 / 40, (-70, -90, 330, 345))],
        model=[os.path.join(P2, "3d", "P2-A-901_RevI_massing.obj"), os.path.join(P2, "3d", "P2-A-901_RevI_massing.mtl")],
        extra=[]),
    "phase1": dict(
        zip="THA_Phase1_CAD_RevA.zip", set_name="Phase 1 Set Rev A (P1-G-001 Rev E, P1-A-101 Rev C, P1-P-001 Rev A, P1-G-002 Rev B)",
        sheets=["P1-G-001_RevE_principal", "P1-A-101_RevC", "P1-P-001_RevA"],
        dxf_dir=os.path.join(P1, "dxf"),
        feet=[("P1-A-101_RevC", 2.15, 2.47, 0.125, (-15, -15, 60, 70))],   # room SW inside corner (p1_a_101_rev_c.py ox, oy), 45 ft E-W x 55 ft N-S
        model=[], extra=["P1-G-002 Rev B (cost sheet) is PDF only: a table, no drawing geometry; no DXF is generated for it."]),
    "phase1mb": dict(
        zip="THA_Phase1_MetalBldg_CAD_RevA.zip", set_name="Phase 1 Metal Building Proposal Set Rev A (D-094; P1-G-101, P1-A-201, P1-A-301, P1-A-901)",
        sheets=["P1-G-101_RevA", "P1-A-201_RevA", "P1-A-301_RevA", "P1-A-901_RevA"],
        dxf_dir=os.path.join(P1, "dxf"),
        feet=[("P1-A-201_RevA", 1.15, 3.77, 0.1, (-15, -15, 115, 75))],   # building SW outside corner (p1_metal_bldg.py ox, oy = bb 2.35 + 1.42), 100 ft E-W x 60 ft N-S
        model=[], extra=["Metal building sizes are ASSUMED (params/phase1_metal_bldg.yaml); frame by Summertown Metals' engineer."]),
}


def to_feet(src, ox, oy, s, win):
    doc = ezdxf.readfile(src)
    m = Matrix44.chain(Matrix44.translate(-ox, -oy, 0), Matrix44.scale(1 / s, 1 / s, 1 / s))
    msp = doc.modelspace()
    x0, y0, x1, y1 = win
    from ezdxf import bbox
    for e in list(msp):
        b = bbox.extents([e], fast=True)
        if not b.has_data:
            msp.delete_entity(e)
            continue
        bx0, by0 = (b.extmin.x - ox) / s, (b.extmin.y - oy) / s
        bx1, by1 = (b.extmax.x - ox) / s, (b.extmax.y - oy) / s
        if bx0 < x0 or by0 < y0 or bx1 > x1 or by1 > y1 or e.dxf.layer.startswith("G-ANNO-TTLB"):
            msp.delete_entity(e)
            continue
        try:
            e.transform(m)
        except Exception:
            msp.delete_entity(e)
    doc.header["$INSUNITS"] = 2          # feet
    doc.header["$MEASUREMENT"] = 0
    doc.header["$LUNITS"] = 4            # architectural
    doc.header["$TDCREATE"] = 2461325.0
    doc.header["$TDUPDATE"] = 2461325.0
    doc.header["$FINGERPRINTGUID"] = "{00000000-0000-0000-0000-000000000000}"
    doc.header["$VERSIONGUID"] = "{00000000-0000-0000-0000-000000000000}"
    st = io.StringIO()
    doc.write(st)
    t = st.getvalue()                    # same bytes on every run: writer stamps, dates and GUIDs fixed
    t = re.sub(r"(\$TD\w+\n\s*40\n)[0-9.]+", r"\g<1>2461325.0", t)
    t = re.sub(r"\{[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}\}", "{00000000-0000-0000-0000-000000000000}", t)
    t = re.sub(r"(\d+\.\d+\.\d+) @ \d{4}-\d\d-\d\dT[0-9:.+]+", r"\1 @ 2026-10-11T00:00:00+00:00", t)
    return t.encode("utf-8"), len(msp)


def layers(path):
    return sorted({e.dxf.layer for e in ezdxf.readfile(path).modelspace()})


def main(which):
    c = SETS[which]
    files, lay = [], set()
    for sname in c["sheets"]:
        p = os.path.join(c["dxf_dir"], sname + ".dxf")
        assert os.path.exists(p), p
        files.append(("sheets_inches/" + sname + ".dxf", open(p, "rb").read()))
        lay |= set(layers(p))
    for sname, ox, oy, s, win in c["feet"]:
        data, n = to_feet(os.path.join(c["dxf_dir"], sname + ".dxf"), ox, oy, s, win)
        files.append(("plans_feet/" + sname + "_MODEL_ft.dxf", data))
        print(f"{sname}: {n} entities in feet")
    for p in c["model"]:
        files.append(("3d/" + os.path.basename(p), open(p, "rb").read()))
    readme = README.format(set_name=c["set_name"], sheets="\n".join("  " + s + ".dxf" for s in c["sheets"]),
                           feet="\n".join(f"  {f[0]}_MODEL_ft.dxf" for f in c["feet"]),
                           model=("\n".join("  " + os.path.basename(p) for p in c["model"]) or "  (none for this phase)"),
                           extra=("\n".join(c["extra"]) or "-"), layers=", ".join(sorted(lay)))
    files.append(("README_CAD.txt", readme.replace("\n", "\r\n").encode("utf-8")))
    out = os.path.join(P2 if which.startswith("phase2") else P1, "pdf", c["zip"])     # next to the combined set PDF
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(files):
            zi = zipfile.ZipInfo(name, date_time=(2026, 10, 11, 0, 0, 0))
            zi.compress_type, zi.external_attr = zipfile.ZIP_DEFLATED, 0o644 << 16
            z.writestr(zi, data)
    print(f"{out}: {len(files)} files, {os.path.getsize(out):,} bytes")


README = """TROJAN HORSE ARENA - CAD FILES - {set_name}
Hazel Green Regional Athletic Complex, Madison County, Alabama (site TBD). Drawn by KEYSTONE (AI) for Shane Brazelton
(256-508-4608, brazeltonshane@gmail.com). Built 2026-10-11 (CT).

PRELIMINARY - CONCEPTUAL DESIGN - NOT FOR CONSTRUCTION. Schematic only. Not a code review; dimensions, heights, column spacing and
materials marked ASSUMED on the sheets are assumptions. A licensed architect / engineer must design, check and seal the work.

UNITS
  plans_feet/*_MODEL_ft.dxf : REAL UNITS, FEET (1 drawing unit = 1 ft; $INSUNITS = 2). Model space, origin 0,0 = the plan grid origin
                              (Phase 2: SW corner of the building grid, x east, y north; Phase 1: room SW inside corner).
                              Plan geometry only: title block, notes and other views on the sheet were left out. Text heights scale with it.
  sheets_inches/*.dxf       : each sheet as drawn, 1 unit = 1 inch on the 11 x 17 sheet (scaled drawings: read the scale on the sheet,
                              e.g. 1/40 in per ft = 1" = 40'). Use these to print / match the PDF.
  3d/*.obj + .mtl           : massing model, units FEET, Z up (A-901). Massing only, not a building model.

FILES
Sheets (inches):
{sheets}
Plans (feet):
{feet}
3D model:
{model}
Note: {extra}

LAYERS (AIA-style names used in these files)
  {layers}

OPENING THE FILES
  AutoCAD: OPEN the DXF directly (units already set). For the feet plans, INSERT / XREF with units = feet.
  Revit: Insert > Link CAD, Import units = Feet (plans_feet) and Positioning = Origin to Origin. Link, don't import, so updates reload.
  SketchUp: File > Import > AutoCAD (*.dxf), Options > Units = Feet. The OBJ also imports (File > Import > OBJ, units feet) in
  SketchUp 2021+ / Revit via a converter / Blender / Rhino.
The PDF set is the record; if a DXF and the PDF differ, the PDF governs.
"""

if __name__ == "__main__":
    main(sys.argv[1])
