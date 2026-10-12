#!/usr/bin/env python3
"""P2-G-001 Rev E: COVER SHEET + SHEET INDEX for Phase 2 Schematic Set Rev F (D-090 colonnade + cleanups; Shane 2026-10-11 7:19 PM CT).
Rev D (Set Rev E cover) kept as is.

New file; G-001 Rev A-C (handoff_2026-10-04/p2_g_001.py, Set Rev D frozen) are not touched. The index lists CURRENT revisions only
(INDEX below; every file is checked to exist). Numbers from p2_plan_rev_n_geom.py and p2_egress_rev_n.py.
  /workspace/.venv-keystone/bin/python blueprints/phase2/src/p2_g_001_rev_d.py --rev D [--out-dir DIR]
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p2_egress_rev_n as eg  # noqa: E402
g, gn = eg.g, eg.gn
sys.path.insert(0, os.path.join(g.ROOT, "blueprints", "shared"))
from palette import SCHOOL_RED  # noqa: E402
from titleblock import Sheet, add_titleblock  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--rev", choices=["E"], required=True)
ap.add_argument("--out-dir", default=os.path.join(g.ROOT, "blueprints", "phase2", "out"))
a = ap.parse_args()
BPD = os.path.join(g.ROOT, "blueprints")
INDEX = [  # sheet, title, rev, file (repo-relative), basis
    ("P2-G-001", "Cover sheet + sheet index", "E", "phase2/out/pdf/P2-G-001_RevE.pdf", "this sheet"),
    ("P2-G-002", "Code analysis — exit recheck", "G", "phase2/out/pdf/P2-G-002_RevG.pdf", "A-101 N / A-102 I; F1 closed"),
    ("P2-G-003", "Program test-fit + areas", "N", "phase2/out/pdf/P2-G-003_RevN.pdf", "D-086"),
    ("P2-C-101", "Site plan — campus diagram", "H", "phase2/out/pdf/P2-C-101_RevH.pdf", "no bus loop (D-087)"),
    ("P2-A-101", "Overall floor plan — Level 1", "N", "phase2/out/pdf/P2-A-101_RevN.pdf", "D-082..D-086"),
    ("P2-A-102", "Overall floor plan — Level 2", "I", "phase2/out/pdf/P2-A-102_RevI.pdf", "D-082, D-083, D-085"),
    ("P2-A-103", "Floor overlays — mats, seating, conversions", "E", "phase2/out/pdf/P2-A-103_RevE.pdf", "notes cite A-101 N / A-111 F"),
    ("P2-A-111", "Life safety plan — Levels 1 + 2", "F", "phase2/out/pdf/P2-A-111_RevF.pdf", "X1-X11; D-090 colonnade"),
    ("P2-A-201", "Exterior elevations — SRM look", "M", "phase2/out/pdf/P2-A-201_RevM.pdf", "D-074, D-090"),
    ("P2-A-301", "Building sections", "F", "phase2/out/pdf/P2-A-301_RevF.pdf", "drum, SRM bands, D-090"),
    ("P2-A-302", "Sight-line study", "C", "phase2/out/pdf/P2-A-302_RevC.pdf", "bowl only; unchanged"),
    ("P2-A-401", "Enlarged plans — lockers + core 2", "E", "phase2/out/pdf/P2-A-401_RevE.pdf", "key plan = A-101 N"),
    ("P2-A-901", "3D massing — SRM look", "H", "phase2/out/pdf/P2-A-901_RevH.pdf", "D-074, D-090"),
    ("P2-SK-01", "Study: mech / elec bay height", "—", "studies/P2-SK-01_MechBay_Height.pdf", "PENDING Shane / architect"),
    ("P2-SK-02", "Study: NE drum height", "—", "studies/P2-SK-02_Drum_Height.pdf", "PENDING Shane / architect"),
]
for row in INDEX[1:]:
    assert os.path.exists(os.path.join(BPD, row[3])), row[3]

W, H = 17.0, 11.0
sh = Sheet(W, H)
top = add_titleblock(sh, dict(
    project="Hazel Green Regional Athletic Complex\nTrojan Horse Arena · Hazel Green area, Madison County, Alabama (site TBD, D-006)",
    phase="PHASE 2", title="COVER SHEET\nSHEET INDEX + DECISIONS", scale="NTS", date="October\n2026",
    revision="E", drawn_by="Drawn by KEYSTONE (AI) for\nShane Brazelton", sheet_no="P2-G-001",
    stamp="PRELIMINARY — CONCEPTUAL DESIGN — NOT FOR CONSTRUCTION"))
GRY = "#555555"
# ---------------------------------------------------------------- left: title block of the set
x0 = 0.85
sh.text(x0, H - 1.5, "TROJAN HORSE ARENA", size=30, bold=True, color=SCHOOL_RED)
sh.text(x0, H - 1.95, "Hazel Green Regional Athletic Complex", size=14, bold=True)
sh.text(x0, H - 2.22, "Hazel Green area, Madison County, Alabama (site TBD, D-006)", size=10)
sh.text(x0, H - 2.75, "PHASE 2 — SCHEMATIC SET · REV F", size=16, bold=True)
sh.text(x0, H - 3.0, "Current design: P2-A-101 Rev N / A-102 Rev I, SRM look (A-201 Rev M, A-901 Rev H)", size=8.5)
y = H - 3.3
sh.text(x0, y, "PROJECT DATA", size=9.5, bold=True)
sh.line(x0, y - 0.05, x0 + 5.2, y - 0.05, lw=0.6)
y -= 0.25
for k, v in [("Building", f"{gn.TOT_N:,} GSF = L1 {gn.L1_N:,} + L2 {gn.L2_N:,} (unchanged since A-101 Rev M)"),
             ("Seats", "2,200 (1,100 telescopic + 1,100 fixed); event floor chairs-only design case (D-054)"),
             ("Exits", "E1 (8 pairs, 512 in) + X1-X11; 4 stairs x 76 in; ST-2 in a 30 ft drum (D-082)"),
             ("Heights", "L2 FF 17'-9\" (D-061); ring roof 32.75', arena roof 42' (ASSUMED)"),
             ("Code basis", "IBC 2021 (ASSUMED edition); AHJ Madison County / State of Alabama TBD (D-008)"),
             ("Status", "PRELIMINARY — conceptual design, not for construction or permit")]:
    sh.text(x0, y, k, size=7.6, bold=True)
    y = sh.para(x0 + 1.0, y + 0.12, 4.25, v, size=7.6) - 0.16
y -= 0.1
sh.text(x0, y, "CONTACT", size=9.5, bold=True)
sh.line(x0, y - 0.05, x0 + 5.2, y - 0.05, lw=0.6)
y -= 0.3
sh.text(x0, y, "Shane Brazelton", size=12, bold=True)
sh.text(x0, y - 0.25, "256-508-4608", size=11)
sh.text(x0, y - 0.48, "brazeltonshane@gmail.com", size=11)
y -= 0.8
y = sh.para(x0, y, 5.2, "GENERAL NOTES: Drawn by KEYSTONE (AI) for Shane Brazelton. Every value not cited is ASSUMED. A licensed architect and engineers must "
            "design, check and seal the work; the AHJ decides code questions (D-008). Supersedes G-001 Rev D (Set Rev E cover).", size=7.2)

# ---------------------------------------------------------------- middle: index
mx = 6.55
y = H - 0.85
sh.text(mx, y, "SHEET INDEX — PHASE 2 SET REV F (current revisions only)", size=10, bold=True)
y -= 0.25
cols = [0, 1.0, 3.95, 4.35]
for dx, t in zip(cols, ["SHEET", "TITLE", "REV", "BASIS"]):
    sh.text(mx + dx, y, t, size=7.6, bold=True)
sh.line(mx, y - 0.05, mx + 6.0, y - 0.05, lw=0.6)
y -= 0.2
for i, (sn, ti, rv, f, basis) in enumerate(INDEX):
    if sn == "P2-SK-01":
        y -= 0.05
        sh.text(mx, y, "APPENDIX — STUDY SHEETS (for decisions, not revisions of the set)", size=7.2, bold=True, color=GRY)
        y -= 0.18
    for dx, t in zip(cols, [sn, ti, rv, basis]):
        sh.text(mx + dx, y, t, size=8.2, bold=(dx == 0))
    y -= 0.215
y -= 0.1
y = sh.para(mx, y, 6.0, "Not current and not in this set: G-001 A-D, G-002 A-F, A-101 A-M, A-102 A-H, A-103 A-D, A-111 A-E, A-201 A-L, A-301 A-E, A-401 A-D, "
            "A-901 A-G, C-101 A-G and Set Rev A-E (archive). The earlier Gemini ARCH D package was superseded and removed.", size=6.8)

# ---------------------------------------------------------------- right: decisions + open items
rx, rw = 12.85, 3.45
y = H - 0.85
sh.text(rx, y, "DESIGN DIRECTION", size=10, bold=True)
sh.line(rx, y - 0.05, rx + rw, y - 0.05, lw=0.6)
y -= 0.12
for t in ["D-074 SRM HQ language: board-formed concrete slab-edge bands with continuous glass per level, no square corners (R 20'), "
          "30' concrete drum with glass slots, slender colonnade + canopy at the lobby, crimson portal. Band levels and canopy 12' ASSUMED.",
          "D-090 Colonnade re-spaced: 2 + 2 columns, entry / portal centre line OPEN, 45.5' centre bay on the portal and walk, 14.5' side bays (ASSUMED); E1 clear 528 in ≥ 512 (PASS).",
          "D-087 Bus loop CUT. Service stays at the north door S1; team bus / van drop-off curbside on the parking drive aisle (ASSUMED, TBD with the parcel, D-006).",
          "D-082..D-086: 30' drum for ST-2, drum door, east side = D-072, landing note, old NE strip = MECH (remote)."]:
    y = sh.para(rx, y, rw, t, size=7.6, bullet="•", indent=0.12) - 0.06
y -= 0.12
sh.text(rx, y, "OPEN DECISIONS", size=10, bold=True, color=SCHOOL_RED)
sh.line(rx, y - 0.05, rx + rw, y - 0.05, lw=0.6)
y -= 0.12
for t in ["SK-01 mech / elec bay height: 16' as drawn (= annex), taller (e.g. 24', A) or full height to the 32.75' ring roof. PENDING.",
          "SK-02 NE drum height: flush with the ring roof as drawn, rising as a tower (e.g. +8', A) or stop at stair / roof-access height. PENDING.",
          f"Mechanical {gn.PCT_N:.2f} % of GSF vs the 5 % target (D-072): {gn.SHORT_N:,.0f} SF short; MEP engineer to size. OPEN.",
          "East-face glazing: the east wall is flush with the 42' arena volume; drawn concrete, no glass (A-201 Rev L, ASSUMED). Glass or not? OPEN.",
          "Egress finding (G-002 Rev G): X6 discharge grading at the NE corner (F2). F1 closed by D-090.",
          "Parcel (D-006), parking ordinance, rooftop solar (zones only), trademark search (D-042), brick pricing (D-044)."]:
    y = sh.para(rx, y, rw, t, size=7.6, bullet="•", indent=0.12) - 0.06
if y < top + 0.2:
    raise SystemExit(f"LAYOUT OVERFLOW: right column {y:.2f}")
print(f"right margin {y - top - 0.2:.2f}")
os.makedirs(os.path.join(a.out_dir, "pdf"), exist_ok=True)
os.makedirs(os.path.join(a.out_dir, "dxf"), exist_ok=True)
sh.render_pdf(os.path.join(a.out_dir, "pdf", "P2-G-001_RevE.pdf"))
sh.render_dxf(os.path.join(a.out_dir, "dxf", "P2-G-001_RevE.dxf"))
