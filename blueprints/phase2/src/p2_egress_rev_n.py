"""Egress recheck on the CURRENT design (P2-A-101 Rev N / A-102 Rev I; D-082..D-087; A-201 Rev L facade). Shared by P2-G-002 Rev F
and P2-A-111 Rev E. No sheet output. Method = P2-G-002 Rev D / E (IBC 2021 T1004.5 factors, 0.15 in/occ. doors, 0.2 in/occ. stairs,
64 in per door pair, T1017.2 250 ft, T1006.2.1 75 ft common path, 1007.1.1 1/3 diagonal). Inputs: p2_plan_rev_n_geom.py (gn / gm)
and params/phase2_facade_srm.yaml (colonnade in front of E1)."""
import math
import os
import sys

import yaml
from shapely.geometry import Point, box
from shapely.ops import unary_union

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p2_plan_rev_n_geom as gn  # noqa: E402

g = gn.gm
J, env = g.J, g.env
FZ = yaml.safe_load(open(os.path.join(g.PAR, "phase2_facade_srm.yaml"), encoding="utf-8"))


def ceil_div(a, f):
    return math.ceil(round(a) / f)


# ---------------------------------------------------------------- Level 1 occupant load (Rev D method, Rev N geometry)
Z = {z["id"]: z["rect"] for z in J["level_1"]["zones"]}
R1 = {r["id"]: r for r in g.L1_ROOMS}


def a(i):
    if i in R1:
        return g.l1_geo(R1[i]).area
    return box(*Z[i]).intersection(env).difference(g.stairs_m).area


MECH = [ar for t, n, ar in gn.mech_rows]
SP = [("Boys + girls locker (2)", a("boys_locker") + a("girls_locker"), 50, 71 + 71),
      ("Event lockers 1-4", sum(a(i) for i in ("evl_1", "evl_2", "evl_3", "evl_4")), 50, 72),
      ("Flex / team assembly", a("team_asm"), 15, ceil_div(a("team_asm"), 15)),
      ("Flex / storage (SW)", a("storage_sw"), 300, ceil_div(a("storage_sw"), 300)),
      ("Equipment storage + room", a("equip_storage") + a("equip_room"), 300, 4),
      ("Mech / elec (%d rooms)" % len(MECH), sum(MECH), 300, sum(ceil_div(m, 300) for m in MECH)),
      ("First aid", a("first_aid"), 150, ceil_div(a("first_aid"), 150)),
      ("Concession", a("concession"), 200, ceil_div(a("concession"), 200)),
      ("Chair / table / stage storage (annex)", g.ANNEX.area, 300, ceil_div(g.ANNEX.area, 300))]
SEATS_L, SEATS_U = 1100, 1100
FIX_L1 = SEATS_L + sum(r[3] for r in SP)
FIX_L1_E = 1467                      # P2-G-002 Rev E
FLOOR_SF = 16416                     # Rev D basis (114 x 144)
CASES = [("Sports (50 gross)", 50), ("Tables + chairs (15 net)", 15), ("Chairs only (7 net) DESIGN", 7), ("Standing (5 net) margin", 5)]

# ---------------------------------------------------------------- Level 2 occupant load (D-052 worst case)
L2S = {n: a1 for t, n, a0, a1 in g.l2_sched}
L2_BASE = SEATS_U + ceil_div(L2S["Strength & Conditioning"], 50) + ceil_div(L2S["Cross-Training Mat"], 50) + ceil_div(L2S["Admin"], 150)
L2_LOOP = ceil_div(L2S["Running / training loop"], 50)
L2_RAIL = 84
L2_WORST = L2_BASE + L2_LOOP + L2_RAIL
L2_WORST_E = 1460                    # P2-G-002 Rev E

# ---------------------------------------------------------------- capacity
DW, DF, SFAC = 64, 0.15, 0.2
E1_IN = g.DOORS["E1"]["bank"]["clear_in"]
EXITS = ["X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11"]
PROV = E1_IN + len(EXITS) * DW
ROWS = []
for lab, fac in CASES:
    fl = ceil_div(FLOOR_SF, fac)
    tot = FIX_L1 + fl + L2_WORST
    ROWS.append(dict(lab=lab, floor=fl, l1=FIX_L1 + fl, tot=tot, req=tot * DF, e1=tot / 2 * DF, lose=0.5 * tot * DF))
ST_REQ = L2_WORST * SFAC
ST_PROV = 4 * 76
ST_DOOR = L2_WORST / 4 * DF

# ---------------------------------------------------------------- exit positions (Rev N)
KX = g.K["exits_moved"]
POS = {}
for d in J["level_1"]["doors"]["items"]:
    i, w, at = d["id"], d["wall"], d["at"]
    if i in ("S1", "E1") or i.startswith("E1"):
        continue
    if i in ("X1", "X10"):
        w, at = "W", KX[i]["at"]
    if i == "X9":
        w, at = "S", KX[i]["at"]
    if i == "X6":
        POS[i] = ("drum E face", g.X6)
        continue
    POS[i] = ({"W": "W wall", "N": "N wall", "E": "E wall", "S": "S wall"}[w], {"W": (0, at), "N": (at, 252), "E": (210, at), "S": (at, 0)}[w])
POS["E1"] = ("S wall bank", (113.0, 0.0))
R_ = 20.0


def on_straight(p):
    x, y = p
    return (R_ <= y <= 252 - R_) if x in (0, 210) else (R_ <= x <= 210 - R_)


CHK = []
for i in EXITS + ["E1"]:
    lab, p = POS[i]
    if i == "X6":
        ok = g.x6_on_drum and g.x6_clear
        note = "ST-2 30 ft drum, east face; clear of bay / annex"
    else:
        db = box(p[0] - 2.67, p[1] - 0.5, p[0] + 2.67, p[1] + 0.5) if p[1] in (0, 252) else box(p[0] - 0.5, p[1] - 2.67, p[0] + 0.5, p[1] + 2.67)
        ok = env.boundary.distance(Point(*p)) < 0.6 and on_straight(p) and db.intersection(unary_union([g.BAY, g.ANNEX, g.BUMP])).area == 0
        note = {"X1": "team assembly (D-078)", "X2": "girls locker", "X3": "boys locker", "X4": "ST-1 discharge", "X5": "EXIT (N), bay clear",
                "X7": "EXIT (E) on the wall, north of the bump-out (D-084)", "X8": "east concourse", "X9": "ST-3 discharge (D-078)",
                "X10": "ST-4 discharge (D-078)", "X11": "public corridor (E), south of the bump-out (D-084)", "E1": "8-pair bank x 87.25-138.75"}[i]
    CHK.append((i, f"{lab} ({p[0]:.1f}, {p[1]:.1f})", note, ok))

# ---------------------------------------------------------------- L1 travel: straight-line worst point to the nearest exit (routed TBD)
PTS = {i: POS[i][1] for i in EXITS}
PTS.update({f"E1_{k}": (87.25 + k * (138.75 - 87.25) / 7, 0.0) for k in range(8)})
worst1, worst1_at = 0.0, None
for xi in range(1, 210, 2):
    for yi in range(1, 252, 2):
        if not env.contains(Point(xi, yi)):
            continue
        d = min(math.hypot(xi - px, yi - py) for px, py in PTS.values())
        if d > worst1:
            worst1, worst1_at = d, (xi, yi)
TRAVEL_L1 = worst1
TRAVEL_L2 = g.TRAVEL_L2
LIM = g.LIM
DIAG = g.DIAG_BLDG
SEP_REQ = DIAG / 3
SEP_MIN = g.SEP_MIN
EAST = g.east
DEAD_END = g.DEAD_END

# ---------------------------------------------------------------- discharge: colonnade in front of E1 (A-201 Rev L, ASSUMED)
co = FZ["colonnade"]
NCOL = int(round((co["x1"] - co["x0"]) / co["spacing_ft"]["value"]))
COL_X = [co["x0"] + k * (co["x1"] - co["x0"]) / NCOL for k in range(NCOL + 1)]
COL_D = co["column_dia_ft"]["value"]
gaps = [(COL_X[k + 1] - COL_X[k] - COL_D) for k in range(NCOL)]
COL_CLEAR_IN = sum(gp for gp in gaps) * 12
COL_GAP_FT = min(gaps)
COL_Y = co["column_line_y"]["value"]
FLAGS = {"travel_l1": TRAVEL_L1 <= LIM["travel_ft"], "travel_l2": TRAVEL_L2 <= LIM["travel_ft"], "sep": SEP_MIN >= SEP_REQ,
         "stairs": ST_PROV >= ST_REQ, "cap": all(PROV >= r["req"] and E1_IN >= r["e1"] for r in ROWS),
         "common": all((EAST[k]["common"] or 0) <= LIM["common_path_ft"] for k in EAST), "dead": DEAD_END <= LIM["dead_end_ft"],
         "exits": all(c[3] for c in CHK), "colonnade": COL_CLEAR_IN >= E1_IN}

if __name__ == "__main__":
    print("L1 fixed", FIX_L1, "(Rev E", FIX_L1_E, ") L2 worst", L2_WORST, "(Rev E", L2_WORST_E, ")")
    for r in ROWS:
        print(r)
    print("stairs req %.1f prov %d; stair door %.1f" % (ST_REQ, ST_PROV, ST_DOOR))
    print("travel L1 %.1f at %s; L2 %.1f; sep %.1f vs %.1f" % (TRAVEL_L1, worst1_at, TRAVEL_L2, SEP_MIN, SEP_REQ))
    print("colonnade gaps", gaps, COL_CLEAR_IN, "E1", E1_IN)
    for c in CHK:
        print(c)
    print(FLAGS, [(s[0], round(s[1]), s[3]) for s in SP])
