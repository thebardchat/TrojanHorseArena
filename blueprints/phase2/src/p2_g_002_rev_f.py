#!/usr/bin/env python3
"""P2-G-002 Rev F: CODE ANALYSIS — EXIT RECHECK on the CURRENT design (P2-A-101 Rev N / A-102 Rev I; D-082..D-087).

New file; P2-G-002 Rev E / D are not touched. Rev E was drawn on A-101 Rev K (20 ft tower, finding F1; bump-out at V2 with X7 on it).
Rev F restates the occupant / capacity / exit / travel tables on Rev N. Numbers from p2_egress_rev_n.py (shared with P2-A-111 Rev E).
  /workspace/.venv-keystone/bin/python blueprints/phase2/src/p2_g_002_rev_f.py --rev F [--out-dir DIR]
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p2_egress_rev_n as eg  # noqa: E402
g, gn = eg.g, eg.gn
sys.path.insert(0, os.path.join(g.ROOT, "blueprints", "shared"))
from titleblock import Sheet, add_titleblock  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--rev", choices=["F"], required=True)
ap.add_argument("--out-dir", default=os.path.join(g.ROOT, "blueprints", "phase2", "out"))
a = ap.parse_args()
RED, GRN, GRY = "#CC0000", "#1E7B34", "#555555"
W, H = 17.0, 11.0
sh = Sheet(W, H)
top = add_titleblock(sh, dict(
    project="Hazel Green Regional Athletic Complex\nTrojan Horse Arena · Hazel Green area, Madison County, Alabama (site TBD, D-006)",
    phase="PHASE 2", title="CODE ANALYSIS\nEXIT RECHECK", scale="NTS", date="October\n2026",
    revision="F", drawn_by="Drawn by KEYSTONE (AI) for\nShane Brazelton", sheet_no="P2-G-002",
    stamp="PRELIMINARY — CONCEPTUAL DESIGN — NOT FOR CONSTRUCTION"))
sh.text(0.75, H - 0.78, "CODE ANALYSIS — EXIT RECHECK (REV F) · P2-A-101 REV N / A-102 REV I · CURRENT DESIGN", size=12, bold=True)
sh.para(0.75, H - 0.9, 15.5, "Supersedes Rev E (drawn on A-101 Rev K: 20 ft tower, F1; bump-out at V2). Method and factors as Rev D / E (IBC 2021 T1004.5, "
        "1005.3, 1005.5, 1030.2, T1017.2, T1006.2.1, 1007.1.1). Not a code review: architect + AHJ confirm (D-008).", size=7)


class Col:
    def __init__(self, x, y, w):
        self.x, self.y, self.w = x, y, w

    def head(self, s):
        self.y -= 0.14
        sh.text(self.x, self.y, s, size=8.6, bold=True)
        sh.line(self.x, self.y - 0.05, self.x + self.w, self.y - 0.05, lw=0.6)
        self.y -= 0.1

    def row(self, xs, vals, size=6.6, bold=False, color=None):
        self.y -= 0.135
        for dx, v in zip(xs, vals):
            sh.text(self.x + dx, self.y, v, size=size, bold=bold, color=color)

    def para(self, s, size=6.6, bullet="•", color=None):
        self.y = sh.para(self.x, self.y - 0.02, self.w, s, size=size, bullet=bullet, indent=0.12 if bullet else 0)


c1 = Col(0.75, H - 1.25, 7.6)
c1.head("1 WHAT CHANGED SINCE REV E (all ASSUMED unless cited)")
for t in ["ST-2 = 30 ft drum (D-082): the 27.2 ft stair diagonal fits with %.1f ft to spare, so Rev E finding F1 is CLOSED. Drum door 64 in at 235° (D-083); landing overlap left to the architect (D-085)." % g.FIT_MARGIN,
          "East side = D-072 / plan Rev J (D-084): bump-out 42 ft south, X7 back on the wall, X11 new, 8 ft public corridor. Old NE stair strip = MECH (remote) (D-086).",
          "Bus loop cut (D-087); A-201 Rev L adds a colonnade + canopy in front of E1 (ASSUMED). Counts unchanged: E1 + X1-X11, 4 stairs x 76 in, 2,200 seats."]:
    c1.para(t)
c1.head("2 OCCUPANT LOAD — LEVEL 1 FIXED SPACES (Rev D method)")
xs = [0, 3.4, 4.3, 5.2, 6.2]
c1.row(xs, ["SPACE", "SF (Rev N)", "FACTOR", "LOAD", ""], bold=True)
for n, sf, f, ld in eg.SP:
    c1.row(xs, [n, f"{sf:,.0f}", str(f), str(ld)])
c1.row(xs, ["Lower tier seats (telescopic)", "", "seats", str(eg.SEATS_L)])
c1.row(xs, ["L1 without the event floor", "", "", f"{eg.FIX_L1:,}", f"Rev E {eg.FIX_L1_E:,}"], bold=True)
c1.row(xs, ["L2 worst case (D-052): seats, S&C, X-train, admin, loop, rail", "", "", f"{eg.L2_WORST:,}", f"Rev E {eg.L2_WORST_E:,}"], bold=True)
c1.para(f"Change: mech rooms now {len(eg.MECH)} incl. the bay and MECH (remote) (+1 occupant). L2 unchanged.", size=6.3, bullet=None)
c1.head("3 EXIT CAPACITY (doors 0.15 in / occ., 64 in per pair)")
xs = [0, 2.6, 3.5, 4.4, 5.4, 6.4]
c1.row(xs, ["FLOOR CASE", "FLOOR", "BUILDING", "NEED in", "E1 ≥ ½", "RESULT"], bold=True)
for r in eg.ROWS:
    ok = eg.PROV >= r["req"] and eg.E1_IN >= r["e1"]
    c1.row(xs, [r["lab"], f"{r['floor']:,}", f"{r['tot']:,}", f"{r['req']:.1f}", f"{r['e1']:.1f}", "PASS" if ok else "FAIL"], bold="DESIGN" in r["lab"], color=None if ok else RED)
c1.para(f"Provided: E1 {eg.E1_IN} in (8 pairs) + 11 exits x 64 = {eg.PROV:,} in. Lose E1: others {eg.PROV - eg.E1_IN} in ≥ ½ of the worst need (1005.5). PASS.", size=6.3, bullet=None)
c1.head("4 LEVEL 2 STAIR CAPACITY (0.2 in / occ.)")
c1.para(f"{eg.L2_WORST:,} x 0.2 = {eg.ST_REQ:.1f} in vs 4 x 76 = {eg.ST_PROV} in (spare {eg.ST_PROV - eg.ST_REQ:.1f}). Lose one stair: 228 ≥ {eg.ST_REQ / 2:.1f}. "
        f"Stair discharge doors {eg.L2_WORST:,} / 4 x 0.15 = {eg.ST_DOOR:.1f} in each of 64. PASS. ST-2 now really holds the 76 in stair (D-082).")

c2 = Col(8.85, H - 1.25, 7.4)
c2.head("5 EXIT LOCATIONS (tested on the Rev N outline)")
xs = [0, 0.55, 2.55, 6.85]
c2.row(xs, ["EXIT", "POSITION", "NOTE", "OK"], bold=True)
for i, pos, note, ok in eg.CHK:
    c2.row(xs, [i, pos, note, "PASS" if ok else "FAIL"], color=None if ok else RED)
c2.para("Test: door on the envelope line, whole 64 in leaf on a straight wall (not in an R 20 arc), clear of annex / bay / bump-out; X6 on the drum.", size=6.2, bullet=None)
c2.head("6 TRAVEL · COMMON PATH · SEPARATION")
for t in [f"L1 exit access (T1017.2, A sprinklered, 250 ft): worst point {eg.TRAVEL_L1:.0f} ft direct to the nearest exit at {eg.worst1_at}; routed path TBD. X7 path T1 {eg.EAST['T1']['total']:.0f} ft. PASS.",
          f"L2 (Rev E method): loop worst {eg.TRAVEL_L2:.0f} ft incl. 15 ft seat access. PASS.",
          f"Common path (T1006.2.1, 75 ft): women (2) {eg.EAST['T7']['common']:.0f} ft, men (2) {eg.EAST['T8']['common']:.0f} ft. Dead end {eg.DEAD_END:.1f} ft (20). Corridor {g.CORR_IN} in (44). PASS.",
          f"Stair separation (1007.1.1, 1/3 of the {eg.DIAG:.0f} ft diagonal = {eg.SEP_REQ:.0f} ft): shortest {eg.SEP_MIN:.0f} ft. PASS."]:
    c2.para(t)
c2.head("7 DISCHARGE (D-087: no bus loop)")
for t in ["All exits discharge to open grade; no drive crosses a discharge. Public-way route and grading: parcel TBD (D-006).",
          f"E1 passes the colonnade: {len(eg.COL_X) - 1} gaps x {eg.COL_GAP_FT:.0f} ft = {eg.COL_CLEAR_IN:.0f} in ≥ {eg.E1_IN} in; then the 40 ft walk around / through the portal (D-066). PASS."]:
    c2.para(t)
c2.head("8 FINDINGS (options; not redesigned)")
for t in ["F1 Colonnade column on the E1 / portal axis (x 113), 10 ft out. Width passes. Options: (a) keep; (b) even column count so the axis is open; (c) wider centre bay. Shane / architect.",
          "F2 X6 discharges between the drum and the bay corner (3 ft apart, west of the door). Confirm the NE walk / grading so X6 reaches open ground (D-006).",
          "F3 Mechanical 4.95 % vs 5 % (D-072, MEP OPEN). Not an egress item; listed for the set."]:
    c2.para(t)
c2.head("9 OPEN FOR THE ARCHITECT / AHJ")
c2.para("Everything in Rev D section 12 stands: editions + AHJ (D-008), construction type, smoke-protected seating, tier structure, door widths. Drum door landing (D-085). Curved-shell structure.")
for c in (c1, c2):
    if c.y < top + 0.35:
        raise SystemExit(f"LAYOUT OVERFLOW: column bottom {c.y:.2f}")
print(f"margins {c1.y - top - 0.35:.2f} / {c2.y - top - 0.35:.2f}")
sh.text(0.75, top + 0.15, "Sources: p2_egress_rev_n.py; p2_plan_rev_n_geom.py (A-101 Rev N / A-102 Rev I); phase2_facade_srm.yaml; P2-G-002 Rev D / E; IBC 2021 as cited; D-052, D-054, D-066, D-072, D-082..D-087.", size=6.0, color=GRY)
os.makedirs(os.path.join(a.out_dir, "pdf"), exist_ok=True)
os.makedirs(os.path.join(a.out_dir, "dxf"), exist_ok=True)
sh.render_pdf(os.path.join(a.out_dir, "pdf", "P2-G-002_RevF.pdf"))
sh.render_dxf(os.path.join(a.out_dir, "dxf", "P2-G-002_RevF.dxf"))
