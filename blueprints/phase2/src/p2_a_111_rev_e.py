#!/usr/bin/env python3
"""P2-A-111 Rev E: LIFE SAFETY PLAN on the CURRENT design (P2-A-101 Rev N / A-102 Rev I; D-082..D-087; A-201 Rev L facade).

New file; P2-A-111 Rev D (Set Rev D, frozen) is not touched. Numbers from p2_egress_rev_n.py (shared with P2-G-002 Rev F).
  /workspace/.venv-keystone/bin/python blueprints/phase2/src/p2_a_111_rev_e.py --rev E [--out-dir DIR]     (run from the repo root)
"""
import argparse
import math
import os
import sys

from shapely.geometry import box

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p2_egress_rev_n as eg  # noqa: E402
g, gn = eg.g, eg.gn
sys.path.insert(0, os.path.join(g.ROOT, "blueprints", "shared"))
from titleblock import Sheet, add_titleblock  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--rev", choices=["E"], required=True)
ap.add_argument("--out-dir", default=os.path.join(g.ROOT, "blueprints", "phase2", "out"))
a = ap.parse_args()

RED, GRN, GRY = "#CC0000", "#1E7B34", "#555555"
J, env = g.J, g.env
W, H = 17.0, 11.0
sh = Sheet(W, H)
top = add_titleblock(sh, dict(
    project="Hazel Green Regional Athletic Complex\nTrojan Horse Arena · Hazel Green area, Madison County, Alabama (site TBD, D-006)",
    phase="PHASE 2", title="LIFE SAFETY PLAN\nLEVELS 1 + 2 · SCHEMATIC", scale="1\" =\n40'-0\"", date="October\n2026",
    revision="E", drawn_by="Drawn by KEYSTONE (AI) for\nShane Brazelton", sheet_no="P2-A-111",
    stamp="PRELIMINARY — CONCEPTUAL DESIGN — NOT FOR CONSTRUCTION"))
S = 1.0 / 40.0
OX, OY = 1.15, top + 1.05


def P(x, y, ox=None, oy=None, sc=None):
    return (ox if ox is not None else OX) + x * (sc or S), (oy if oy is not None else OY) + y * (sc or S)


def poly(geo, fill=None, lw=0.6, layer="A-ROOM", **k):
    if geo.is_empty:
        return
    for gg in ([geo] if geo.geom_type == "Polygon" else list(geo.geoms)):
        sh.poly([P(x, y, **k) for x, y in gg.exterior.coords], fill=fill, lw=lw, layer=layer)


def label(x, y, s, size=6, bold=False, color=None, align="center", **k):
    px, py = P(x, y, **k)
    sh.text(px, py - size / 72 * 0.35, s, size=size, bold=bold, align=align, color=color, layer="A-ANNO-TEXT")


# ---------------------------------------------------------------- LEVEL 1
sh.text(4.35, top + 0.62, "LEVEL 1 — LIFE SAFETY (P2-A-101 REV N)", size=10, bold=True)
sh.text(4.35, top + 0.45, "1\" = 40'-0\" · exits X1-X11 + E1, travel, common path, discharge · no bus loop (D-087)", size=6.5, color=GRY)
for z in J["level_1"]["zones"]:
    poly(box(*z["rect"]).intersection(env).difference(g.stairs_m), fill="#F3F1EC", lw=0.2)
for r in g.L1_ROOMS:
    poly(g.l1_geo(r) if r["id"] not in g.BUMP_ROOMS else box(*r["rect"]), fill="#E4E1D8", lw=0.3)
poly(box(*J["event_floor"]["rect"]), fill="#F1E6CC", lw=0.4)
poly(gn.STRIP, fill="#E4E1D8", lw=0.3)
for geo in (g.ST1, g.ST3, g.ST4, g.drum):
    poly(geo, fill="#B9B3A0", lw=0.8, layer="A-STAIR")
for geo in (g.ANNEX, g.BAY, g.BUMP):
    poly(geo, fill="#C9CCD0", lw=0.9, layer="A-ANNEX")
ext = list(env.exterior.coords)
for (ax_, ay_), (bx_, by_) in zip(ext, ext[1:]):
    (x1, y1), (x2, y2) = P(ax_, ay_), P(bx_, by_)
    sh.line(x1, y1, x2, y2, layer="A-WALL-EXT", lw=2.0)
for (sid, geo) in (("ST-1", g.ST1), ("ST-3", g.ST3), ("ST-4", g.ST4)):
    c = geo.centroid
    label(c.x, c.y, sid, size=5.2, bold=True)
label(g.DC[0], g.DC[1], "ST-2", size=5.2, bold=True)
label(87, 267, "ANNEX", size=5, bold=True)
label(149, 267, "BAY", size=5, bold=True)
label(225, 147, "CORE 2", size=4.6, bold=True)
label(116, 140, "EVENT FLOOR", size=7, bold=True)
label(116, 133, "chairs only 7 net = design case (D-054)", size=5.2)

# exits: red bar + tag + outward discharge arrow (green)
OUT = {"W wall": (-1, 0), "N wall": (0, 1), "E wall": (1, 0), "S wall": (0, -1), "drum E face": (1, 0), "S wall bank": (0, -1)}
for i, (lab, (x, y)) in eg.POS.items():
    dx, dy = OUT[lab]
    if i == "E1":
        a0, a1 = P(87.25, 0), P(138.75, 0)
        sh.line(a0[0], a0[1], a1[0], a1[1], layer="A-EXIT", lw=3.0)
    else:
        h = 64 / 24.0
        a0 = P(x - h * abs(dy), y - h * abs(dx))
        a1 = P(x + h * abs(dy), y + h * abs(dx))
        sh.line(a0[0], a0[1], a1[0], a1[1], layer="A-EXIT", lw=3.0)
    L = 14 if i != "E1" else 8
    p0, p1 = P(x + dx * 1.5, y + dy * 1.5), P(x + dx * L, y + dy * L)
    sh.line(p0[0], p0[1], p1[0], p1[1], layer="A-EXIT-DISCH", lw=0.8)
    ux, uy = (p1[0] - p0[0]), (p1[1] - p0[1])
    n = math.hypot(ux, uy) or 1
    ux, uy = ux / n, uy / n
    sh.poly([p1, (p1[0] - ux * 0.08 - uy * 0.04, p1[1] - uy * 0.08 + ux * 0.04), (p1[0] - ux * 0.08 + uy * 0.04, p1[1] - uy * 0.08 - ux * 0.04)],
            fill=GRN, lw=0, layer="A-EXIT-DISCH")
    tx, ty = P(x + dx * (L + 6), y + dy * (L + 6))
    if i == "E1":
        tx, ty = P(150, -5)
    sh.text(tx, ty - 0.03, i if i != "E1" else "E1 512\"", size=5.6, bold=True, align="center" if i != "E1" else "left", color=RED, layer="A-EXIT")
# colonnade + portal piers in front of E1 (A-201 Rev L, C-101 Rev H)
for cx_ in eg.COL_X:
    c0 = P(cx_, eg.COL_Y)
    sh.poly([(c0[0] + eg.COL_D / 2 * S * math.cos(t / 8 * 2 * math.pi), c0[1] + eg.COL_D / 2 * S * math.sin(t / 8 * 2 * math.pi)) for t in range(8)], fill="#777777", lw=0.2, layer="A-COLS")
pt = {"center_x": 113, "width": 44, "depth": 6, "gap": 30}
op = 28
for x0_, x1_ in ((pt["center_x"] - pt["width"] / 2, pt["center_x"] - op / 2), (pt["center_x"] + op / 2, pt["center_x"] + pt["width"] / 2)):
    poly(box(x0_, -pt["gap"] - pt["depth"], x1_, -pt["gap"]), fill="#CC0000", lw=0.4, layer="A-PORTAL")
label(113, -41, "PORTAL (piers) · walk 40' (D-066)", size=4.6)
label(60, -14, f"colonnade {len(eg.COL_X)} cols, {eg.COL_GAP_FT:.0f}' gaps (ASSUMED)", size=4.6, color=GRY)
# travel paths (red dashed) + worst L1 point
for pth in g.ES["paths"]:
    pts = pth["pts"]
    for (ax_, ay_), (bx_, by_) in zip(pts, pts[1:]):
        (x1, y1), (x2, y2) = P(ax_, ay_), P(bx_, by_)
        sh.dashed(x1, y1, x2, y2, layer="A-EXIT-TRAVEL", lw=0.7, dash=0.06, gap=0.04)
    q = P(*pts[0])
    sh.text(q[0] + 0.03, q[1] + 0.03, pth["id"], size=5, bold=True, color=RED)
wx, wy = eg.worst1_at
q = P(wx, wy)
sh.poly([(q[0] - 0.04, q[1]), (q[0], q[1] + 0.04), (q[0] + 0.04, q[1]), (q[0], q[1] - 0.04)], fill=RED, lw=0)
sh.text(q[0] + 0.06, q[1] - 0.12, f"L1 worst point, {eg.TRAVEL_L1:.0f}' direct to the nearest exit", size=5, color=RED)
# north arrow
nx, ny = P(262, 40)
sh.line(nx, ny, nx, ny + 0.45, lw=1.0)
sh.poly([(nx - 0.06, ny + 0.33), (nx, ny + 0.47), (nx + 0.06, ny + 0.33)], fill="#000000", lw=0)
sh.text(nx, ny + 0.53, "N", size=9, bold=True, align="center")

# ---------------------------------------------------------------- LEVEL 2 (small)
S2 = 1.0 / 80.0
OX2, OY2 = 7.95, top + 4.6
kw = dict(ox=OX2, oy=OY2, sc=S2)
sh.text(OX2, OY2 - 0.3, "LEVEL 2 — STAIRS + LOOP (P2-A-102 REV I) · 1\" = 80'", size=8.5, bold=True)
poly(env, fill="#F3F1EC", lw=1.2, **kw)
for ob in g.open_ob:
    poly(ob, fill="#FFFFFF", lw=0.4, **kw)
poly(g.loop, fill="#E9D7A8", lw=0.3, **kw)
for geo in (g.ST1, g.ST3, g.ST4, g.drum):
    poly(geo, fill="#B9B3A0", lw=0.6, **kw)
for sid, (x, y) in (("ST-1", (42.667, 240)), ("ST-2", g.DC), ("ST-3", (183.667, 12)), ("ST-4", (6.3, 32))):
    label(x, y + (9 if sid != "ST-3" else -11), sid, size=5, bold=True, **kw)
label(116, 140, "OPEN TO ARENA", size=5, color=GRY, **kw)
label(116, 128, f"loop worst {eg.TRAVEL_L2:.0f}' (incl. 15' seat access)", size=4.8, color=RED, **kw)

# ---------------------------------------------------------------- right panel
RX, RW = 11.45, 5.05
y = H - 0.78


def head(t):
    global y
    y -= 0.06
    sh.text(RX, y, t, size=8, bold=True)
    sh.line(RX, y - 0.04, RX + RW, y - 0.04, lw=0.5)
    y -= 0.16


def row(cols, vals, size=6.4, bold=False, color=None):
    global y
    for x, v in zip(cols, vals):
        sh.text(x, y, v, size=size, bold=bold, color=color)
    y -= 0.13


head("EXITS (each tested on the Rev N outline)")
cols = [RX, RX + 0.42, RX + 1.95, RX + 4.75]
row(cols, ["EXIT", "POSITION", "SERVES", "OK"], bold=True)
for i, pos, note, ok in eg.CHK:
    row(cols, [i, pos.replace(" wall", ""), note[:40], "PASS" if ok else "FAIL"], color=None if ok else RED)
head("CAPACITY (doors 0.15 in/occ., 64 in per pair; stairs 0.2)")
cols = [RX, RX + 1.85, RX + 2.6, RX + 3.35, RX + 4.2]
row(cols, ["FLOOR CASE", "BLDG OCC.", "NEED in", "E1 ½", "PROVIDED"], bold=True)
for r in eg.ROWS:
    row(cols, [r["lab"][:28], f"{r['tot']:,}", f"{r['req']:.1f}", f"{r['e1']:.1f}", f"{eg.PROV:,} / E1 {eg.E1_IN}"], bold="DESIGN" in r["lab"])
row([RX], [f"L2 worst {eg.L2_WORST:,} x 0.2 = {eg.ST_REQ:.1f} in vs 4 x 76 = {eg.ST_PROV} in; lose one stair 228 in. PASS."])
head("TRAVEL · COMMON PATH · SEPARATION (IBC 2021)")
for t in [f"L1 travel (T1017.2, 250 ft): worst point {eg.TRAVEL_L1:.0f} ft direct to the nearest exit (routed path TBD). X7 path T1 {eg.EAST['T1']['total']:.0f} ft. PASS.",
          f"L2 travel: loop worst {eg.TRAVEL_L2:.0f} ft. PASS.",
          f"Common path (75 ft): women (2) {eg.EAST['T7']['common']:.0f} ft, men (2) {eg.EAST['T8']['common']:.0f} ft. Dead end {eg.DEAD_END:.1f} ft (20). PASS.",
          f"Stair separation (1007.1.1, 1/3 x {eg.DIAG:.0f} = {eg.SEP_REQ:.0f} ft): shortest {eg.SEP_MIN:.0f} ft (ST-1 to ST-2 drum door). PASS."]:
    y = sh.para(RX, y + 0.05, RW, t, size=6.4, bullet="•", indent=0.12) - 0.05
head("DISCHARGE (no bus loop, D-087)")
for t in ["Every exit discharges straight to open grade; no bus loop or drive crosses a discharge. Route to a public way: parcel TBD (D-006).",
          f"E1: through the colonnade ({len(eg.COL_X) - 1} gaps x {eg.COL_GAP_FT:.0f} ft = {eg.COL_CLEAR_IN:.0f} in clear vs {eg.E1_IN} in bank) and around / through the portal on the 40 ft walk (D-066).",
          "X5 in the 12 ft lane between annex and bay; X6 off the drum east face (3 ft drum-to-bay gap is west of it); X7 / X11 to grade east (D-084)."]:
    y = sh.para(RX, y + 0.05, RW, t, size=6.4, bullet="•", indent=0.12) - 0.05
head("FINDINGS (not redesigned)")
for t in ["F1 A colonnade column sits on the E1 / portal axis (x 113), 10 ft in front of the centre door pairs. Width still passes. Options: (a) keep; (b) even column count so the axis is open; (c) wider centre bay. Shane / architect.",
          "F2 X6 opens toward the bay corner (drum-to-bay 3 ft): the landing outside X6 faces east, clear; confirm grading / walk at the NE corner (D-006)."]:
    y = sh.para(RX, y + 0.05, RW, t, size=6.4, bullet="•", indent=0.12) - 0.05
_ys = sh.para(RX, top + 0.42, RW, "Sources: p2_egress_rev_n.py (P2-G-002 Rev F); p2_plan_rev_n_geom.py; phase2_facade_srm.yaml; phase2_site.yaml portal; D-054, D-066, D-072, D-078, D-082..D-087.", size=5.0)
if y < top + 0.55:
    raise SystemExit(f"LAYOUT OVERFLOW: right panel {top + 0.55 - y:.2f} in")
print(f"right panel margin {y - top - 0.55:.2f} in")
os.makedirs(os.path.join(a.out_dir, "pdf"), exist_ok=True)
os.makedirs(os.path.join(a.out_dir, "dxf"), exist_ok=True)
sh.render_pdf(os.path.join(a.out_dir, "pdf", "P2-A-111_RevE.pdf"))
sh.render_dxf(os.path.join(a.out_dir, "dxf", "P2-A-111_RevE.dxf"))
g.true_circle_dxf(os.path.join(a.out_dir, "dxf", "P2-A-111_RevE.dxf"), P, S)
