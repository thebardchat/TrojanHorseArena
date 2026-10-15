#!/usr/bin/env python3
"""KEYSTONE Phase 1 ALTERNATE, REV B (D-095 supersedes the D-094 layout): new pre-engineered metal building (Summertown Metals) on HGHS property.
60 x 125 ft (ASSUMED): wrestling mat room (west), N-S + E-W corridors, girls' flag football locker room + boys wrestling locker room (ASSUMED),
each with its own team showers / toilets (doors from the locker room and the corridor), women's + men's restrooms off the corridor, office, storage, JAN.
All inputs from params/phase1_metal_bldg_rev_b.yaml. Rev A (p1_metal_bldg.py) stays frozen.

  /workspace/.venv-keystone/bin/python blueprints/phase1/src/p1_metal_bldg_rev_b.py --sheet A-201 --rev B [--out-dir DIR]
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import yaml
from shapely.geometry import box
from shapely.ops import unary_union

BP = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BP / "shared"))
from titleblock import Sheet, add_titleblock  # noqa: E402
from palette import SCHOOL_RED, INK_MUTED, TINT_BLUE, TINT_SAND, TINT_GREEN, STEEL  # noqa: E402

P = yaml.safe_load((BP / "params" / "phase1_metal_bldg_rev_b.yaml").read_text(encoding="utf-8"))
P1 = yaml.safe_load((BP / "params" / "phase1.yaml").read_text(encoding="utf-8"))
W, H = 17.0, 11.0
GRY = INK_MUTED
B = P["building"]
L, D = B["length_ft"]["value"], B["width_ft"]["value"]
EAVE, PITCH = B["eave_ft"]["value"], B["roof_pitch"]["value"] / 12.0
RIDGE = EAVE + D / 2 * PITCH
WT = B["wall_in"]["value"] / 12.0
IT = P["layout"]["thick_in"] / 12.0
FRAMES = [i * B["bay_ft"]["value"] for i in range(int(L / B["bay_ft"]["value"]) + 1)]
ECOLS = [i * B["endwall_col_ft"]["value"] for i in range(int(D / B["endwall_col_ft"]["value"]) + 1)]
ROOMS = {r["id"]: r for r in P["layout"]["rooms"]}
WR = box(*P["wrestling"]["rect"])
DOORS = P["doors"]
DMAP = {d["id"]: d for d in DOORS}
PS = 0.09375                                   # plan scale in / ft (3/32" = 1'-0")
SHEETS = {
    "G-101": ("P1-G-101", "COVER + CODE SUMMARY\nMETAL BUILDING (ALT.)", "NTS"),
    "A-201": ("P1-A-201", "FLOOR PLAN\nMETAL BUILDING (ALT.)", "3/32\" = 1'-0\""),
    "A-301": ("P1-A-301", "ELEVATIONS + SECTION\nMETAL BUILDING (ALT.)", "1/16\" = 1'-0\""),
    "A-901": ("P1-A-901", "3D MASSING\nMETAL BUILDING (ALT.)", "NTS"),
}


def area(r):
    return (r[2] - r[0]) * (r[3] - r[1])


def plen(pts):
    return sum(abs(b[0] - a[0]) + abs(b[1] - a[1]) for a, b in zip(pts[:-1], pts[1:]))


# ---------------------------------------------------------------- numbers (shared by all sheets)
def occ():
    rows = [("Wrestling mat room", WR.area, P["wrestling"]["occ_factor"]["value"])]
    for r in P["layout"]["rooms"]:
        if r["factor"]:
            rows.append((r["label"].title().replace("'S", "'s"), area(r["rect"]), r["factor"]))
    out = [(n, a, f, math.ceil(a / f - 1e-9)) for n, a, f in rows]
    return out, sum(o[3] for o in out)


OCC, TOTAL = occ()
R_ = P["fixtures"]["ratios"]
HALF = math.ceil(TOTAL / 2)
NEED = dict(wc_f=math.ceil(HALF / R_["wc_f"]), wc_m=math.ceil(HALF / R_["wc_m"]), lav_f=math.ceil(HALF / R_["lav_f"]),
            lav_m=math.ceil(HALF / R_["lav_m"]), df=math.ceil(TOTAL / R_["df"]), ss=1)
PV = P["fixtures"]["provided"]
PROV = dict(wc_f=PV["womens_rr"]["wc"] + PV["girls_team"]["wc"], wc_m=PV["mens_rr"]["wc"] + PV["boys_team"]["wc"], ur=PV["mens_rr"]["urinal"],
            lav_f=PV["womens_rr"]["lav"] + PV["girls_team"]["lav"], lav_m=PV["mens_rr"]["lav"] + PV["boys_team"]["lav"],
            sh=PV["girls_team"]["showers"] + PV["boys_team"]["showers"], df=PV["df"], ss=PV["service_sink"])
EXITS = [d for d in DOORS if d["exit"]]
EX_IN = sum(d["width_in"] for d in EXITS)
NEED_IN = TOTAL * P["code"]["egress_in_per_occ"]["value"]
TRAVEL = [(t["name"], t["exit"], plen(t["pts"])) for t in P["travel_paths"]["list"]]
CPATH = [(t["name"], plen(t["pts"])) for t in P["travel_paths"]["common_path"]]
FLAGS = dict(travel=max(t[2] for t in TRAVEL) <= P["code"]["travel_ft"]["value"], cpath=max(c[1] for c in CPATH) <= P["code"]["common_path_ft"]["value"],
             width=EX_IN >= NEED_IN, wc_f=PROV["wc_f"] >= NEED["wc_f"], wc_m=PROV["wc_m"] >= NEED["wc_m"],
             lav=PROV["lav_f"] >= NEED["lav_f"] and PROV["lav_m"] >= NEED["lav_m"], df=PROV["df"] >= NEED["df"],
             area=L * D <= 9500, mat_exits=3 >= 2)
# every restroom / team toilet room has a corridor door (D-095 rule)
CORR_DOOR = {"girls_sh": "GC", "boys_sh": "BC", "womens": "WR", "mens": "MR"}
assert all(DMAP[v]["wall"] in ("Y34", "Y26") for v in CORR_DOOR.values())


def tb(sh, key):
    no, title, scale = SHEETS[key]
    m = P1["meta"]
    return add_titleblock(sh, dict(project=f"{m['project']}\nHazel Green HS · Phase 1 alternate: new metal training building",
                                   phase="PHASE 1\nALTERNATE", title=title, scale=scale, date=P["meta"]["date"], revision=P["meta"]["revision"],
                                   drawn_by=m["drawn_by"].replace(" for ", " for\n"), sheet_no=no, stamp=m["stamp"]))


def note_col(sh, x, y, w, items, size=7.0):
    for t in items:
        y = sh.para(x, y, w, t, size=size, bullet="•", indent=0.12) - 0.05
    return y


def circ(sh, T, cx, cy, r, n=32, **k):
    sh.poly([T(cx + r * math.cos(a / n * 2 * math.pi), cy + r * math.sin(a / n * 2 * math.pi)) for a in range(n)], **k)


# fixtures for the north (girls / women) rooms; south rooms are mirrored about y = 30
FIX_N = {
    "girls_sh": [((97.0, 53.6, 103.6, 59.6), "ACC WC"), ((90.4, 57.4, 93.4, 59.6), "LAV"), ((100.6, 34.4, 103.6, 37.4), "SH"),
                 ((100.6, 37.9, 103.6, 40.9), "SH"), ((100.6, 41.4, 103.6, 44.4), "SH"), ((90.4, 40.0, 95.4, 43.0), "ACC SH")],
    "womens": [((108.6, 53.6, 113.6, 59.6), "ACC WC"), ((110.6, 48.6, 113.6, 53.1), "WC"), ((104.4, 55.0, 106.4, 57.0), "LAV"),
               ((104.4, 51.6, 106.4, 53.6), "LAV")],
}
FIX_S = {"boys_sh": FIX_N["girls_sh"],
         "mens": [((108.6, 53.6, 113.6, 59.6), "ACC WC"), ((112.2, 50.0, 113.6, 52.0), "UR"), ((104.4, 55.0, 106.4, 57.0), "LAV")]}


def mir(r):
    return (r[0], 60 - r[3], r[2], 60 - r[1])


# ---------------------------------------------------------------- P1-A-201 floor plan
def plan(sh, ox, oy, s, full=True):
    T = lambda x, y: (ox + x * s, oy + y * s)  # noqa: E731
    R = lambda r, **k: sh.poly([T(r[0], r[1]), T(r[2], r[1]), T(r[2], r[3]), T(r[0], r[3])], **k)  # noqa: E731
    tint = {"sand": TINT_SAND, "blue": TINT_BLUE, "none": "#FFFFFF"}
    R(P["wrestling"]["rect"], fill="#EFEFEF", layer="A-FLOR-PATT", lw=0)
    for c in P["layout"]["corridors"]:
        R(c["rect"], fill=TINT_GREEN, layer="A-FLOR-PATT", lw=0)
    for r in P["layout"]["rooms"]:
        R(r["rect"], fill=tint[r["tint"]], layer="A-FLOR-PATT", lw=0)
    m = P["wrestling"]["mat"]["rect"]
    R(m, fill="#C9302C", layer="A-FLOR-MATS", lw=0.5)
    cx, cy = (m[0] + m[2]) / 2, (m[1] + m[3]) / 2
    circ(sh, T, cx, cy, 14, 48, fill="#E8E8E8", layer="A-FLOR-MATS", lw=0.5)
    circ(sh, T, cx, cy, 5, 32, fill="#C9302C", layer="A-FLOR-MATS", lw=0.4)
    pad = 0.6
    for r in ((WT, WT, 50 - IT / 2, WT + pad), (WT, D - WT - pad, 50 - IT / 2, D - WT), (WT, WT, WT + pad, D - WT), (50 - IT / 2 - pad, WT, 50 - IT / 2, D - WT)):
        R(r, fill="#2B2B2B", layer="A-FLOR-PADS", lw=0)
    # walls: shell + every room / corridor outline (6 in), minus door openings
    shell = box(0, 0, L, D).difference(box(WT, WT, L - WT, D - WT))
    rects = [P["wrestling"]["rect"]] + [r["rect"] for r in P["layout"]["rooms"]]
    inner = unary_union([box(*r).exterior.buffer(IT / 2, cap_style=3, join_style=2) for r in rects]).intersection(box(0, 0, L, D))
    walls = shell.union(inner)
    ops = []
    for d_ in DOORS:
        w = d_["width_in"] / 12.0
        k = d_["wall"]
        if k in ("S", "N"):
            y0 = 0 if k == "S" else D - WT
            ops.append(box(d_["at"] - w / 2, y0 - 0.1, d_["at"] + w / 2, y0 + WT + 0.1))
        elif k in ("W", "E"):
            x0 = 0 if k == "W" else L - WT
            ops.append(box(x0 - 0.1, d_["at"] - w / 2, x0 + WT + 0.1, d_["at"] + w / 2))
        elif k[0] == "X":
            x = float(k[1:])
            ops.append(box(x - IT, d_["at"] - w / 2, x + IT, d_["at"] + w / 2))
        else:
            y = float(k[1:])
            ops.append(box(d_["at"] - w / 2, y - IT, d_["at"] + w / 2, y + IT))
    walls = walls.difference(unary_union(ops))
    for g in getattr(walls, "geoms", [walls]):
        sh.poly([T(x, y) for x, y in g.exterior.coords], fill="#1A1A1A", layer="A-WALL", lw=0.3)
        for hole in g.interiors:
            sh.poly([T(x, y) for x, y in hole.coords], fill="#FFFFFF", layer="A-WALL", lw=0.3)
    # door leaves: exits swing out; Y26 doors swing south into rooms, Y34 north into rooms, X doors east
    for d_ in DOORS:
        w = d_["width_in"] / 12.0
        n = 2 if d_["width_in"] >= 60 else 1
        lw_ = w / n
        k = d_["wall"]
        if k in ("S", "N") or k[0] == "Y":
            yb = {"S": 0, "N": D}.get(k, float(k[1:]) if k[0] == "Y" else 0)
            sgn = -1 if k == "S" else 1 if k == "N" else (1 if yb > 30 else -1)
            hinges = [(d_["at"] - w / 2, 1)] + ([(d_["at"] + w / 2, -1)] if n == 2 else [])
            for hx, dirn in hinges:
                sh.line(*T(hx, yb), *T(hx, yb + sgn * lw_), layer="A-DOOR", lw=0.5)
                pts = [T(hx + dirn * lw_ * math.sin(a / 12 * math.pi / 2), yb + sgn * lw_ * math.cos(a / 12 * math.pi / 2)) for a in range(13)]
                for p0, p1 in zip(pts[:-1], pts[1:]):
                    sh.line(*p0, *p1, layer="A-DOOR", lw=0.25)
        else:
            if k in ("W", "E"):
                sgn, xb = (-1, 0) if k == "W" else (1, L)
            else:
                xb, sgn = float(k[1:]), 1
            hinges = [(d_["at"] - w / 2, 1)] + ([(d_["at"] + w / 2, -1)] if n == 2 else [])
            for hy, dirn in hinges:
                sh.line(*T(xb, hy), *T(xb + sgn * lw_, hy), layer="A-DOOR", lw=0.5)
                pts = [T(xb + sgn * lw_ * math.cos(a / 12 * math.pi / 2), hy + dirn * lw_ * math.sin(a / 12 * math.pi / 2)) for a in range(13)]
                for p0, p1 in zip(pts[:-1], pts[1:]):
                    sh.line(*p0, *p1, layer="A-DOOR", lw=0.25)
    if not full:
        return T
    for i, x in enumerate(FRAMES):
        sh.dashed(*T(x, -4), *T(x, D + 4), layer="S-GRID", lw=0.3, dash=0.1, gap=0.05)
        bx, by = T(x, D + 6)
        circ(sh, lambda a, b: (a, b), bx, by, 0.11, 16, fill="#FFFFFF", layer="S-GRID", lw=0.4)
        sh.text(bx, by - 0.04, str(i + 1), size=6.5, bold=True, align="center", layer="S-GRID")
        sh.rect(*T(x - 0.6, -0.6), 1.2 * s, 1.2 * s, layer="S-COLS", lw=0.6)
        sh.rect(*T(x - 0.6, D - 0.6), 1.2 * s, 1.2 * s, layer="S-COLS", lw=0.6)
    for j, y in enumerate(ECOLS):
        sh.dashed(*T(-4, y), *T(0, y), layer="S-GRID", lw=0.3, dash=0.1, gap=0.05)
        bx, by = T(-6, y)
        circ(sh, lambda a, b: (a, b), bx, by, 0.11, 16, fill="#FFFFFF", layer="S-GRID", lw=0.4)
        sh.text(bx, by - 0.04, "ABCD"[j], size=6.5, bold=True, align="center", layer="S-GRID")

    def dim_h(x0, x1, y, txt):
        sh.line(*T(x0, y), *T(x1, y), layer="A-ANNO-DIMS", lw=0.35)
        for xx in (x0, x1):
            sh.line(*T(xx, y - 0.8), *T(xx, y + 0.8), layer="A-ANNO-DIMS", lw=0.35)
        a, b = T((x0 + x1) / 2, y + 0.8)
        sh.text(a, b, txt, size=6.0, align="center", layer="A-ANNO-DIMS")
    dim_h(0, L, -10, f"{L:g}'-0\" OUT TO OUT (ASSUMED)")
    for x0, x1 in zip(FRAMES[:-1], FRAMES[1:]):
        dim_h(x0, x1, -6, f"{x1 - x0:g}'-0\" BAY")
    sh.line(*T(L + 7, 0), *T(L + 7, D), layer="A-ANNO-DIMS", lw=0.35)
    for yy in (0, D):
        sh.line(*T(L + 6.2, yy), *T(L + 7.8, yy), layer="A-ANNO-DIMS", lw=0.35)
    a, b = T(L + 8.2, D / 2)
    sh.text(a, b, f"{D:g}'-0\" CLEAR SPAN", size=6.0, rot=90, align="center", layer="A-ANNO-DIMS")

    def tag(x, y, t1, t2=None, size=6.6, color=None):
        a, b = T(x, y)
        sh.text(a, b, t1, size=size, bold=True, align="center", layer="A-ANNO-TEXT", color=color)
        if t2:
            sh.text(a, b - 0.14, t2, size=5.2, align="center", layer="A-ANNO-TEXT", color=GRY)
    o = {n: oc for n, a, f, oc in OCC}
    tag(25, 55.2, "WRESTLING MAT ROOM", f"{WR.area:,.0f} SF · {o['Wrestling mat room']} occ. (50 gross)", size=7.6)
    tag(25, 4.0, "42' x 42' MAT · 28' CIRCLE (NFHS 2-1-2)", "6' wall pads all walls · LED high-bay", size=6.4)
    tag(54, 45, "CORR.", "8'", size=5.6)
    tag(77, 30.6, "E-W CORRIDOR 8'", None, size=5.6)
    big = {"girls_lr": ("GIRLS FLAG FOOTBALL", "LOCKER ROOM", "(ASSUMED)"), "boys_lr": ("BOYS WRESTLING", "LOCKER ROOM", "(ASSUMED — CONFIRM)")}
    for rid, (a1, a2, a3) in big.items():
        r = ROOMS[rid]["rect"]
        cy_ = 48 if rid == "girls_lr" else 12
        tag((r[0] + r[2]) / 2 + 3, cy_ + 3.4, a1, None, size=6.4)
        tag((r[0] + r[2]) / 2 + 3, cy_ + 1.6, a2, f"{area(r):,.0f} SF · {math.ceil(area(r) / 50)} occ. {a3}", size=6.4)
    small = {"girls_sh": ("GIRLS TEAM", "SHOWER / WC"), "boys_sh": ("BOYS TEAM", "SHOWER / WC"), "womens": ("WOMEN'S", "RESTROOM"),
             "mens": ("MEN'S", "RESTROOM"), "office": ("COACHES'", "OFFICE"), "storage": ("STORAGE", None), "jan": ("JAN./MECH", None)}
    for rid, (a1, a2) in small.items():
        r = ROOMS[rid]["rect"]
        mx = (r[0] + r[2]) / 2
        my = {"girls_sh": 49.5, "boys_sh": 10.5, "womens": 45.0, "mens": 15.0, "office": 48.5, "storage": 20.0, "jan": 7.0}[rid]
        a, b = T(mx, my)
        sh.text(a, b, a1, size=5.4, bold=True, align="center", layer="A-ANNO-TEXT")
        if a2:
            sh.text(a, b - 0.12, a2, size=5.4, bold=True, align="center", layer="A-ANNO-TEXT")
        sh.text(a, b - (0.24 if a2 else 0.12), f"{area(r):,.0f} SF", size=4.8, align="center", layer="A-ANNO-TEXT", color=GRY)
    # lockers + benches (girls drawn, boys mirrored)
    for mirror in (False, True):
        f = mir if mirror else (lambda r: r)
        for r, horiz in (((58 + IT / 2, 58.75, 89.6, 60 - WT), True), ((58 + IT / 2, 35.0, 59.25 + IT / 2, 57.5), False)):
            rr = f(r)
            R(rr, fill="#9AA5B1", layer="A-FURN", lw=0.3)
            nn = int(round(((rr[2] - rr[0]) if horiz else (rr[3] - rr[1])) / 1.5))
            for k in range(1, nn):
                if horiz:
                    xx = rr[0] + k * (rr[2] - rr[0]) / nn
                    sh.line(*T(xx, rr[1]), *T(xx, rr[3]), layer="A-FURN", lw=0.15)
                else:
                    yy = rr[1] + k * (rr[3] - rr[1]) / nn
                    sh.line(*T(rr[0], yy), *T(rr[2], yy), layer="A-FURN", lw=0.15)
        for r in ((66, 43, 80, 44.75), (66, 52.5, 80, 54.25)):
            R(f(r), fill="#D2B48C", layer="A-FURN", lw=0.3)
        a, b = T(74, 56.6 if not mirror else 2.6)
        sh.text(a, b, f"{20 + 15} LOCKERS 18\" x 15\" (30 + 2 ACC., ASSUMED) · 2 BENCHES (1 ACC.)", size=4.6, align="center", layer="A-FURN", color=GRY)
    for fix, mirror in ((FIX_N, False), (FIX_S, True)):
        for rid, lst in fix.items():
            for r, lab in lst:
                rr = mir(r) if mirror else r
                R(rr, fill="#DCEBF7" if "SH" in lab else "#FFFFFF", layer="P-FIXT", lw=0.4)
                a, b = T((rr[0] + rr[2]) / 2, (rr[1] + rr[3]) / 2 - 0.4)
                sh.text(a, b, lab, size=3.8, align="center", layer="P-FIXT")
            tc = {"girls_sh": (96.5, 46.5), "womens": (108.5, 41.0)}.get(rid if not mirror else {"boys_sh": "girls_sh", "mens": "womens"}[rid])
            circ(sh, T, tc[0], 60 - tc[1] if mirror else tc[1], 2.5, 24, fill=None, layer="P-FIXT", lw=0.25)
    R((50 + IT / 2 + 0.1, 40, 51.4, 43.5), fill="#FFFFFF", layer="P-FIXT", lw=0.4)
    a, b = T(52.4, 41.3)
    sh.text(a, b, "DF hi-lo", size=4.4, layer="P-FIXT")
    R((122.6, 0.5 + WT, 124.6 - WT + 0.6, 2.5 + WT), fill="#FFFFFF", layer="P-FIXT", lw=0.4)
    for d_ in DOORS:
        k = d_["wall"]
        p = {"S": (d_["at"], -2.8), "N": (d_["at"], D + 1.4), "W": (-2.6, d_["at"] + 3.0), "E": (L + 2.6, d_["at"] + 4.5)}.get(k)
        if p is None:
            continue
        a, b = T(*p)
        sh.text(a, b, d_["id"] + (" EXIT" if d_["exit"] else ""), size=5.4, bold=True, align="center", layer="A-ANNO-EXIT", color=SCHOOL_RED if d_["exit"] else None)
    a, b = T(L + 11.5, D - 2)
    sh.poly([(a, b + 0.32), (a - 0.1, b), (a + 0.1, b)], fill="#1A1A1A", layer="A-ANNO-TEXT", lw=0.3)
    sh.text(a, b - 0.17, "N", size=8, bold=True, align="center", layer="A-ANNO-TEXT")
    return T


PLAN_OX, PLAN_DY = 1.0, 1.42


def sheet_a201():
    sh = Sheet(W, H)
    bb = tb(sh, "A-201")
    s, ox, oy = PS, PLAN_OX, bb + PLAN_DY
    plan(sh, ox, oy, s)
    sh.text(ox, oy - 1.16, "FLOOR PLAN — NEW METAL TRAINING BUILDING (ALTERNATE) REV B", size=10.5, bold=True)
    sh.text(ox, oy - 1.31, f"3/32\" = 1'-0\" · {L:g}' x {D:g}' = {L * D:,.0f} SF clear-span PEMB, 5 x 25' bays (ASSUMED) · plan north up · D-095", size=6.6, color=GRY)
    x, w = 14.15, 2.4
    sh.line(x - 0.1, H - 0.6, x - 0.1, bb + 0.1, lw=0.4)
    y = H - 0.75
    sh.text(x, y, "PLAN NOTES", size=8.5, bold=True)
    y -= 0.08
    y = note_col(sh, x, y, w, [
        "D-095 (Shane 2026-10-15 5:12 AM CT) supersedes the D-094 layout: restrooms open off the corridor; 2 locker rooms, each with its own showers.",
        f"Grown one 25' bay: 60' x 100' -> {D:g}' x {L:g}' (ASSUMED). Mat room unchanged: 42' x 42' mat, 6' pads.",
        "North: girls' flag football locker room (ASSUMED). South: boys wrestling locker room (ASSUMED — CONFIRM: Shane wrote 'boys lockeroom and boys locker room for wrestling').",
        "Team shower / WC rooms: doors from the locker room AND the E-W corridor. Women's + men's restrooms open only off the corridor.",
        "Privacy vestibules / door hardware at the corridor doors TBD (architect).",
        "Exits (red): D1 main pair, D2 N, D3 W, D4 mat pair, D5 E corridor pair. Checks: P1-G-101.",
        "Wet walls TBD (CMU or moisture-resistant). Cost TBD per the Summertown Metals quote.",
    ], size=6.0)
    y -= 0.05
    sh.text(x, y, "LEGEND", size=7.5, bold=True)
    y -= 0.18
    for col, t in (("#C9302C", "wrestling mat"), ("#2B2B2B", "6' wall pads"), (TINT_SAND, "locker rooms"), (TINT_BLUE, "showers / restrooms"),
                   (TINT_GREEN, "corridors"), ("#9AA5B1", "lockers")):
        sh.poly([(x, y), (x + 0.22, y), (x + 0.22, y + 0.12), (x, y + 0.12)], fill=col, lw=0.3)
        sh.text(x + 0.3, y + 0.02, t, size=5.8)
        y -= 0.17
    if y < bb + 0.1:
        raise SystemExit(f"LAYOUT OVERFLOW: A-201 notes {bb + 0.1 - y:.2f} in")
    return sh

# ---------------------------------------------------------------- P1-A-301 elevations + section
def elev(sh, ox, oy, s, face):
    """face S / N (length L, sidewall) or E / W (gable, width D). x measured left-to-right as seen."""
    T = lambda u, z: (ox + u * s, oy + z * s)  # noqa: E731
    span = L if face in ("S", "N") else D
    if face in ("S", "N"):
        sh.poly([T(0, 0), T(span, 0), T(span, EAVE), T(0, EAVE)], fill="#D8DCE0", layer="A-ELEV-SKIN", lw=0.8)
        sh.poly([T(-1, EAVE), T(span + 1, EAVE), T(span + 1, RIDGE), T(-1, RIDGE)], fill=STEEL, layer="A-ELEV-ROOF", lw=0.6)
    else:
        sh.poly([T(0, 0), T(span, 0), T(span, EAVE), T(span / 2, RIDGE), T(0, EAVE)], fill="#D8DCE0", layer="A-ELEV-SKIN", lw=0.8)
        sh.line(*T(-1, EAVE - 1 * PITCH), *T(span / 2, RIDGE + 0.3), layer="A-ELEV-ROOF", lw=1.4)
        sh.line(*T(span / 2, RIDGE + 0.3), *T(span + 1, EAVE - 1 * PITCH), layer="A-ELEV-ROOF", lw=1.4)
    # panel ribs
    for k in range(1, int(span / 3)):
        u = k * 3
        top = EAVE if face in ("S", "N") else min(EAVE + (u if u <= span / 2 else span - u) * PITCH, RIDGE)
        sh.line(*T(u, 0.2), *T(u, top - 0.1), layer="A-ELEV-SKIN", lw=0.12)
    # daylight band (translucent panels 12-14 ft, ASSUMED)
    sh.poly([T(1, 12), T(span - 1, 12), T(span - 1, 14), T(1, 14)], fill="#F3F0D8", layer="A-ELEV-GLAZ", lw=0.3)
    # wainscot (crimson accent 0-3 ft, ASSUMED school color)
    sh.poly([T(0, 0), T(span, 0), T(span, 3), T(0, 3)], fill="#9E1B1B", layer="A-ELEV-SKIN", lw=0.3)
    # doors on this face
    for d_ in DOORS:
        if d_["wall"] != face:
            continue
        w = d_["width_in"] / 12.0
        u = d_["at"] if face in ("S", "W") else (L - d_["at"] if face == "N" else D - d_["at"])
        if face == "W":
            u = D - d_["at"]
        if face == "E":
            u = d_["at"]
        sh.poly([T(u - w / 2, 0), T(u + w / 2, 0), T(u + w / 2, 7), T(u - w / 2, 7)], fill="#FFFFFF", layer="A-ELEV-DOOR", lw=0.6)
        if w > 4:
            sh.line(*T(u, 0), *T(u, 7), layer="A-ELEV-DOOR", lw=0.4)
        a, b = T(u, 7.6)
        sh.text(a, b, d_["id"], size=5, bold=True, align="center", color=SCHOOL_RED if d_["exit"] else None, layer="A-ELEV-DOOR")
    if face == "N":                                   # coaches' office window (x 116-123)
        sh.poly([T(L - 123, 4), T(L - 116, 4), T(L - 116, 8), T(L - 123, 8)], fill="#BFD7EA", layer="A-ELEV-GLAZ", lw=0.5)
    sh.line(*T(-3, 0), *T(span + 3, 0), layer="A-ELEV-GRND", lw=1.2)
    for z, lab in ((EAVE, f"EAVE {EAVE:g}'-0\" (A)"), (RIDGE, f"RIDGE {RIDGE:.2f}' (1:12)") if face in ("E", "W") else (None, None), (0, "FF 0'-0\"")):
        if z is None:
            continue
        a, b = T(span + 3.5, z)
        sh.line(*T(span + 1.5, z), *T(span + 3.2, z), layer="A-ELEV-DATM", lw=0.3)
        sh.text(a, b - 0.03, lab, size=5.0, layer="A-ELEV-DATM")
    return T


def section(sh, ox, oy, s):
    T = lambda u, z: (ox + u * s, oy + z * s)  # noqa: E731
    hb = 2.2                                          # tapered column / rafter depth at the knee (ASSUMED)
    sh.poly([T(-0.5, 0), T(0.6, 0), T(0.6 + 0.6, EAVE - hb), T(0.6 + hb, EAVE - 0.4), T(D / 2, RIDGE - 1.6), T(D / 2, RIDGE), T(-0.5, EAVE)],
            fill="#7F8C99", layer="S-FRAM", lw=0.5)
    sh.poly([T(D + 0.5, 0), T(D - 0.6, 0), T(D - 1.2, EAVE - hb), T(D - 0.6 - hb, EAVE - 0.4), T(D / 2, RIDGE - 1.6), T(D / 2, RIDGE), T(D + 0.5, EAVE)],
            fill="#7F8C99", layer="S-FRAM", lw=0.5)
    sh.line(*T(-1, EAVE), *T(D / 2, RIDGE + 0.2), layer="A-SECT-ROOF", lw=1.2)
    sh.line(*T(D / 2, RIDGE + 0.2), *T(D + 1, EAVE), layer="A-SECT-ROOF", lw=1.2)
    sh.line(*T(-4, 0), *T(D + 4, 0), layer="A-SECT-GRND", lw=1.4)
    sh.poly([T(9, 0), T(51, 0), T(51, 0.5), T(9, 0.5)], fill="#C9302C", layer="A-SECT-MATS", lw=0.3)
    for u in (0.7, D - 1.3):
        sh.poly([T(u, 0), T(u + 0.6, 0), T(u + 0.6, 6), T(u, 6)], fill="#2B2B2B", layer="A-SECT-PADS", lw=0.2)
    for u in (12, 24, 36, 48):
        a, b = T(u, EAVE - 1.5)
        sh.poly([(a - 0.06, b), (a + 0.06, b), (a + 0.04, b - 0.05), (a - 0.04, b - 0.05)], fill="#F2C94C", layer="E-LITE", lw=0.2)
    sh.dashed(*T(3, B["clear_ft"]["value"]), *T(D - 3, B["clear_ft"]["value"]), layer="A-SECT-DATM", lw=0.4)
    a, b = T(D / 2, B["clear_ft"]["value"] - 1.4)
    sh.text(a, b, f"{B['clear_ft']['value']:g}' MIN CLEAR UNDER FRAME (ASSUMED)", size=5.2, align="center", color=SCHOOL_RED, layer="A-SECT-DATM")
    a, b = T(D / 2, 1.2)
    sh.text(a, b, "42' MAT · 6' WALL PADS · LED HIGH-BAY", size=5.0, align="center", layer="A-SECT-MATS")
    a, b = T(D / 2, -2.6)
    sh.text(a, b, f"{D:g}'-0\" CLEAR SPAN (no interior columns)", size=5.4, align="center", layer="A-ANNO-DIMS")
    return T


def sheet_a301():
    sh = Sheet(W, H)
    bb = tb(sh, "A-301")
    s = 1 / 16
    top = H - 0.7
    blocks = [("SOUTH ELEVATION (MAIN ENTRY)", "S", 0.9, top - 1.75), ("NORTH ELEVATION", "N", 0.9, top - 3.55),
              ("EAST ELEVATION (LOCKER END)", "E", 10.6, top - 1.75), ("WEST ELEVATION (MAT ROOM END)", "W", 10.6, top - 3.55)]
    for t, f, x, y in blocks:
        elev(sh, x, y, s, f)
        sh.text(x, y - 0.32, f"{t} — 1/16\" = 1'-0\"", size=7.6, bold=True)
    section(sh, 0.9 + 0.2, top - 6.35, s * 1.6)
    sh.text(0.9, top - 6.75, "SECTION A-A THROUGH THE MAT ROOM (looking west) — 1/10\" = 1'-0\"", size=7.6, bold=True)
    x, w = 9.2, 7.2
    y = top - 4.25
    sh.line(x - 0.15, y + 0.15, x - 0.15, bb + 0.1, lw=0.4)
    sh.text(x, y, "NOTES", size=9, bold=True)
    y = note_col(sh, x, y - 0.1, w, [
        f"Pre-engineered clear-span rigid frame, 1:12 gable (ASSUMED). Eave {EAVE:g}' (ASSUMED), ridge {RIDGE:.2f}' computed from the pitch. Final frame, eave and clear height by Summertown Metals' engineer.",
        "Walls / roof: insulated metal panels (IMP or metal + liner, Summertown kit), R-values per the Alabama Energy Code (IECC 2015 / 90.1-2013) — TBD by supplier (R-028.4).",
        "Daylight: translucent wall-panel band 12'-14' (ASSUMED) on all faces; skylights only where code / supplier allow (D-093 direction). LED high-bay in the mat room; LED elsewhere.",
        "Color: crimson wainscot 0-3' (school color, ASSUMED); light gray panels; dark roof (ASSUMED). Gutters / downspouts to rain capture if the campus wants it (unsized).",
        "Doors: hollow-metal exit doors with panic hardware on D1-D5 (Group A, IBC 1010.2.9); D5 = east corridor pair; JD = JAN. / mech service door (not an exit). Red tags = exits. D-095 Rev B: 60' x 125', 5 bays (ASSUMED).",
        "Foundation: slab-on-grade with column piers / anchor bolts per the PEMB reactions — geotech + structural TBD. No site plan yet (location on campus TBD).",
    ], size=6.6)
    if y < bb + 0.1:
        raise SystemExit(f"LAYOUT OVERFLOW: A-301 notes {bb + 0.1 - y:.2f} in")
    return sh


# ---------------------------------------------------------------- P1-A-901 massing (isometric, painter's order)
def iso(x, y, z, ox, oy, s):
    a = math.radians(30)
    return (ox + (x + y) * math.cos(a) * s, oy + ((y - x) * math.sin(a) + z) * s)


def massing(sh, ox, oy, s, view="SE"):
    if view == "SE":                                  # look from the SE: swap so +x goes right, y away (mirror y)
        Pf = lambda x, y, z: iso(x, y, z, ox, oy, s)  # noqa: E731
    else:
        Pf = lambda x, y, z: iso(L - x, D - y, z, ox, oy, s)  # noqa: E731
    poly = lambda pts, **k: sh.poly([Pf(*p) for p in pts], **k)  # noqa: E731
    # ground shadow
    poly([(-3, -3, 0), (L + 3, -3, 0), (L + 3, D + 3, 0), (-3, D + 3, 0)], fill="#EEEEEE", layer="A-MASS-GRND", lw=0)
    if view == "SE":
        # roof north plane (far), east gable, south wall, roof south plane
        poly([(0, D, EAVE), (L, D, EAVE), (L, D / 2, RIDGE), (0, D / 2, RIDGE)], fill="#4A4A4A", layer="A-MASS-ROOF", lw=0.4)
        poly([(0, 0, 0), (L, 0, 0), (L, 0, EAVE), (0, 0, EAVE)], fill="#D8DCE0", layer="A-MASS-WALL", lw=0.6)
        poly([(0, 0, 0), (L, 0, 0), (L, 0, 3), (0, 0, 3)], fill="#9E1B1B", layer="A-MASS-WALL", lw=0.3)
        poly([(1, 0, 12), (L - 1, 0, 12), (L - 1, 0, 14), (1, 0, 14)], fill="#F3F0D8", layer="A-MASS-GLAZ", lw=0.3)
        poly([(L, 0, 0), (L, D, 0), (L, D, EAVE), (L, D / 2, RIDGE), (L, 0, EAVE)], fill="#C4C9CE", layer="A-MASS-WALL", lw=0.6)
        poly([(L, 0, 0), (L, D, 0), (L, D, 3), (L, 0, 3)], fill="#861717", layer="A-MASS-WALL", lw=0.3)
        poly([(0, 0, EAVE), (L, 0, EAVE), (L, D / 2, RIDGE), (0, D / 2, RIDGE)], fill="#5B5B5B", layer="A-MASS-ROOF", lw=0.5)
        for d_ in DOORS:
            if d_["wall"] == "S":
                w = d_["width_in"] / 12
                poly([(d_["at"] - w / 2, 0, 0), (d_["at"] + w / 2, 0, 0), (d_["at"] + w / 2, 0, 7), (d_["at"] - w / 2, 0, 7)], fill="#FFFFFF", layer="A-MASS-DOOR", lw=0.4)
            if d_["wall"] == "E":
                w = d_["width_in"] / 12
                poly([(L, d_["at"] - w / 2, 0), (L, d_["at"] + w / 2, 0), (L, d_["at"] + w / 2, 7), (L, d_["at"] - w / 2, 7)], fill="#FFFFFF", layer="A-MASS-DOOR", lw=0.4)
        # canopy over D1 (ASSUMED)
        poly([(48, 0, 9), (60, 0, 9), (60, -6, 9), (48, -6, 9)], fill="#9E1B1B", layer="A-MASS-CANO", lw=0.4)
    else:
        # from the NW: north wall + west gable visible
        poly([(0, 0, EAVE), (L, 0, EAVE), (L, D / 2, RIDGE), (0, D / 2, RIDGE)], fill="#4A4A4A", layer="A-MASS-ROOF", lw=0.4)
        poly([(0, D, 0), (L, D, 0), (L, D, EAVE), (0, D, EAVE)], fill="#C4C9CE", layer="A-MASS-WALL", lw=0.6)
        poly([(0, D, 0), (L, D, 0), (L, D, 3), (0, D, 3)], fill="#861717", layer="A-MASS-WALL", lw=0.3)
        poly([(1, D, 12), (L - 1, D, 12), (L - 1, D, 14), (1, D, 14)], fill="#F3F0D8", layer="A-MASS-GLAZ", lw=0.3)
        poly([(0, 0, 0), (0, D, 0), (0, D, EAVE), (0, D / 2, RIDGE), (0, 0, EAVE)], fill="#D8DCE0", layer="A-MASS-WALL", lw=0.6)
        poly([(0, 0, 0), (0, D, 0), (0, D, 3), (0, 0, 3)], fill="#9E1B1B", layer="A-MASS-WALL", lw=0.3)
        poly([(0, D, EAVE), (L, D, EAVE), (L, D / 2, RIDGE), (0, D / 2, RIDGE)], fill="#5B5B5B", layer="A-MASS-ROOF", lw=0.5)
        for d_ in DOORS:
            w = d_["width_in"] / 12
            if d_["wall"] == "N":
                poly([(d_["at"] - w / 2, D, 0), (d_["at"] + w / 2, D, 0), (d_["at"] + w / 2, D, 7), (d_["at"] - w / 2, D, 7)], fill="#FFFFFF", layer="A-MASS-DOOR", lw=0.4)
            if d_["wall"] == "W":
                poly([(0, d_["at"] - w / 2, 0), (0, d_["at"] + w / 2, 0), (0, d_["at"] + w / 2, 7), (0, d_["at"] - w / 2, 7)], fill="#FFFFFF", layer="A-MASS-DOOR", lw=0.4)
    return Pf


def sheet_a901():
    sh = Sheet(W, H)
    bb = tb(sh, "A-901")
    top = H - 0.75
    Pf = massing(sh, 1.6, bb + 1.7 + 65 * 0.5 * 0.046, 0.046, "SE")
    sh.text(0.8, top, "V1  AERIAL FROM THE SOUTHEAST (main entry + locker end)", size=9, bold=True)
    sh.text(0.8, top - 0.18, "isometric · not to scale · massing only", size=6.4, color=GRY)
    for (x, y, z), dx, dy, t in (((25, 0, 8), -0.4, -0.8, "MAT ROOM (west) — D3 / D4 exits"), ((54, -6, 9), -0.5, -1.0, "D1 MAIN ENTRY + canopy (ASSUMED)"),
                                 ((L, 30, 6), 0.6, -0.3, "LOCKER END — D5 corridor exit pair"), ((50, D / 2, RIDGE), 0.2, 0.7, f"1:12 gable, ridge {RIDGE:.2f}' (ASSUMED)"),
                                 ((70, 0, 13), 1.9, -0.25, "translucent daylight band 12'-14' (ASSUMED)"), ((112, 0, 1.5), 0.9, -0.3, "crimson wainscot 0-3' (ASSUMED)")):
        a, b = Pf(x, y, z)
        sh.line(a, b, a + dx, b + dy, lw=0.35)
        sh.text(a + dx + (0.04 if dx > 0 else -0.04), b + dy - 0.03, t, size=6.0, align="left" if dx > 0 else "right")
    massing(sh, 11.4, bb + 4.9 + 65 * 0.5 * 0.028, 0.028, "NW")
    sh.text(11.4, top, "V2  FROM THE NORTHWEST (mat room end, D2 / D3)", size=8, bold=True)
    x, w = 11.4, 5.0
    y = bb + 3.7
    sh.text(x, y, "NOTES", size=9, bold=True)
    y = note_col(sh, x, y - 0.1, w, [
        f"Massing only: {L:g}' x {D:g}' x {EAVE:g}' eave pre-engineered metal building (ASSUMED sizes, D-095 Rev B) from params/phase1_metal_bldg_rev_b.yaml.",
        "Summertown Metals kit (frame, panels, trim, doors). Colors, canopy and daylight band ASSUMED for discussion.",
        "Not modelled: site, grading, walks, parking, MEP units, gutters. Location on the HGHS campus TBD with Madison County Schools.",
        "Cost TBD per the supplier quote (no prices in this set).",
    ], size=6.6)
    if y < bb + 0.1:
        raise SystemExit("LAYOUT OVERFLOW: A-901 notes")
    return sh


# ---------------------------------------------------------------- P1-G-101 cover + code summary
def sheet_g101():
    sh = Sheet(W, H)
    bb = tb(sh, "G-101")
    x0, y = 0.8, H - 0.95
    sh.text(x0, y, "HAZEL GREEN HS WRESTLING + FLAG FOOTBALL", size=13, bold=True, color=SCHOOL_RED)
    sh.text(x0, y - 0.38, "New metal training building — PROPOSAL SET REV B", size=9.5, bold=True)
    y = sh.para(x0, y - 0.62, 5.4, f"Replaces the old 55' x 45' wrestling room (10' ceiling) at Hazel Green High School, 14380 Hwy 231-431 N, Hazel Green, AL 35750 (Madison County Schools property; location on campus TBD). Supplier: {P['supplier']['name']}, {P['supplier']['address']}, {P['supplier']['phone']} (quote TBD).", size=7.4)
    y -= 0.1
    sh.text(x0, y, "SHEET INDEX", size=9, bold=True)
    y -= 0.22
    for no, t in (("P1-G-101", "Cover + code summary"), ("P1-A-201", "Floor plan"), ("P1-A-301", "Elevations + section"), ("P1-A-901", "3D massing")):
        sh.text(x0, y, no, size=7.4, bold=True)
        sh.text(x0 + 1.0, y, t + " — Rev B (Rev A superseded)", size=7.4)
        y -= 0.19
    y -= 0.08
    sh.text(x0, y, "PROJECT DATA (ASSUMED unless cited)", size=9, bold=True)
    y -= 0.08
    rr = ROOMS
    y = note_col(sh, x0, y, 5.4, [
        f"Building {D:g}' x {L:g}' = {L * D:,.0f} SF, 1 storey, clear span, 5 x 25' bays, eave {EAVE:g}', {B['clear_ft']['value']:g}' min clear, 1:12 gable.",
        "D-095 (Shane 2026-10-15 5:12 AM CT) supersedes the D-094 layout: restrooms off the corridor; boys wrestling locker room added (ASSUMED — confirm wording); each locker room has its own showers.",
        f"Rooms: wrestling mat room {WR.area:,.0f} SF (42' x 42' mat) · girls' flag football locker {area(rr['girls_lr']['rect']):,.0f} SF · boys wrestling locker {area(rr['boys_lr']['rect']):,.0f} SF · 2 team shower / WC rooms {area(rr['girls_sh']['rect']):,.0f} SF each · women's + men's restrooms {area(rr['womens']['rect']):,.0f} SF each · coaches' office {area(rr['office']['rect']):,.0f} SF · storage {area(rr['storage']['rect']):,.0f} SF · JAN. / mech {area(rr['jan']['rect']):,.0f} SF · 8' N-S + E-W corridors.",
        "Remodel set (P1-G-001 Rev E, P1-A-101 Rev C, P1-G-002 Rev B) stays the base option.",
        "Cost: TBD per the Summertown Metals quote + site, foundation, MEP, permit, design. No prices invented.",
        "Contact: Shane Brazelton, 256-508-4608, brazeltonshane@gmail.com.",
    ], size=7.0)
    cx = 6.6
    sh.line(cx - 0.15, H - 0.6, cx - 0.15, bb + 0.1, lw=0.4)
    y = H - 0.75
    sh.text(cx, y, "CODE SUMMARY — IBC / IPC 2021 (AHJ to confirm)", size=9, bold=True)
    y -= 0.08
    c = P["code"]
    y = note_col(sh, cx, y, 4.9, [f"Occupancy: {c['occupancy']['text']} (ASSUMED).", f"Construction: {c['construction']['text']} (ASSUMED).",
                                  f"Area: {c['allowable']['text']}: {'PASS' if FLAGS['area'] else 'CHECK'}.", f"Sprinklers: {c['sprinkler']['text']}."], size=6.8)
    y -= 0.05
    sh.text(cx, y, "OCCUPANT LOAD (IBC 2021 Table 1004.5)", size=7.6, bold=True)
    y -= 0.2
    for n, a, f, oc in OCC:
        sh.text(cx, y, n, size=6.6)
        sh.text(cx + 3.3, y, f"{a:,.0f} SF / {f}", size=6.6, align="right")
        sh.text(cx + 4.1, y, f"{oc}", size=6.6, align="right")
        y -= 0.17
    sh.text(cx, y, "TOTAL (restrooms / showers / corridors accessory)", size=6.6, bold=True)
    sh.text(cx + 4.1, y, f"{TOTAL}", size=6.6, bold=True, align="right")
    y -= 0.27
    sh.text(cx, y, "EGRESS", size=7.6, bold=True)
    y -= 0.08
    wt = max(TRAVEL, key=lambda t: t[2])
    wc = max(CPATH, key=lambda t: t[1])
    y = note_col(sh, cx, y, 4.9, [
        f"Width: {TOTAL} x {c['egress_in_per_occ']['value']} in = {NEED_IN:.1f} in needed (1005.3.2) vs {EX_IN} in of exit doors (D1-D5): {'PASS' if FLAGS['width'] else 'CHECK'}.",
        f"Mat room {OCC[0][3]} occ. > 49: 2 exits needed (1006.2.1); 3 provided (D3, D4, corridor I1): PASS. Each locker room {math.ceil(area(ROOMS['boys_lr']['rect']) / 50)} occ.: 1 door to the corridor, then 2 directions.",
        f"Travel (Table 1017.2, {c['travel_ft']['value']} ft non-sprinklered): worst {wt[2]:.0f} ft ({wt[0]} to {wt[1]}, routes ASSUMED): {'PASS' if FLAGS['travel'] else 'CHECK'}.",
        f"Common path (Table 1006.2.1, {c['common_path_ft']['value']} ft): worst {wc[1]:.0f} ft ({wc[0]}): {'PASS' if FLAGS['cpath'] else 'CHECK'}.",
        "Exit doors: panic hardware (1010.2.9); exit signs + egress lighting (1008, 1013).",
    ], size=6.6)
    fx = 11.85
    sh.line(fx - 0.15, H - 0.6, fx - 0.15, bb + 0.1, lw=0.4)
    y = H - 0.75
    sh.text(fx, y, "PLUMBING FIXTURES — IPC 2021 Table 2902.1", size=9, bold=True)
    y -= 0.08
    y = sh.para(fx, y, 4.6, f"Basis: {P['fixtures']['basis']['text']} (ASSUMED). {TOTAL} occ. -> {HALF} F + {HALF} M.", size=6.6) - 0.08
    rows = [("WC — female", f"1:{R_['wc_f']}", NEED["wc_f"], f"{PROV['wc_f']} (2 RR + 1 team)", FLAGS["wc_f"]),
            ("WC — male", f"1:{R_['wc_m']}", NEED["wc_m"], f"{PROV['wc_m']} + {PROV['ur']} UR", FLAGS["wc_m"]),
            ("Lavatory F / M", f"1:{R_['lav_f']} / 1:{R_['lav_m']}", f"{NEED['lav_f']} / {NEED['lav_m']}", f"{PROV['lav_f']} / {PROV['lav_m']}", FLAGS["lav"]),
            ("Drinking fountain", f"1:{R_['df']}", NEED["df"], f"{PROV['df']} (hi-lo)", FLAGS["df"]),
            ("Service sink", "1", NEED["ss"], f"{PROV['ss']} (JAN.)", True),
            ("Showers", "not req. (A-3)", 0, f"{PROV['sh']} (4 + 4, 2 acc.)", True)]
    for t in (("FIXTURE", 0), ("RATIO", 1.2), ("REQ.", 2.55), ("PROVIDED", 3.05)):
        sh.text(fx + t[1], y, t[0], size=6.2, bold=True)
    y -= 0.18
    for n, rr_, req, prov, ok in rows:
        sh.text(fx, y, n, size=6.2)
        sh.text(fx + 1.2, y, rr_, size=6.2)
        sh.text(fx + 2.6, y, str(req), size=6.2)
        sh.text(fx + 3.05, y, prov + (" PASS" if ok else " CHECK"), size=6.2)
        y -= 0.17
    y = sh.para(fx, y - 0.03, 4.6, "D-095: every restroom and both team shower / WC rooms have a door on the corridor; the women's / men's restrooms serve the public and visiting teams without entering a locker room.", size=6.0) - 0.1
    sh.text(fx, y, "OPEN ITEMS / FINDINGS", size=8, bold=True, color=SCHOOL_RED)
    y -= 0.08
    y = note_col(sh, fx, y, 4.6, [
        "CONFIRM: second locker room = boys wrestling (ASSUMED from 'boys lockeroom and boys locker room for wrestling'). If Shane meant a separate boys locker room too, a 3rd room needs another bay (60' x 150').",
        "Team / rosters: girls' flag football 30 + boys wrestling 30 ASSUMED.",
        "Size 60' x 125' (grown from 60' x 100'): Shane to confirm.",
        "Location on campus, utilities (water / sewer), geotech: TBD with Madison County Schools.",
        "Sprinklers / fire alarm: AHJ + district. Supplier quote: Summertown Metals (kit only).",
    ], size=6.3)
    if y < bb + 0.1:
        raise SystemExit("LAYOUT OVERFLOW: G-101")
    return sh


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", choices=list(SHEETS), required=True)
    ap.add_argument("--rev", choices=["B"], required=True)
    ap.add_argument("--out-dir")
    ap.add_argument("--print", action="store_true")
    a = ap.parse_args()
    if a.print:
        print(OCC, TOTAL, NEED, PROV, EX_IN, NEED_IN, TRAVEL, CPATH, FLAGS)
        return
    no = SHEETS[a.sheet][0]
    sh = {"G-101": sheet_g101, "A-201": sheet_a201, "A-301": sheet_a301, "A-901": sheet_a901}[a.sheet]()
    od = Path(a.out_dir) if a.out_dir else BP / "phase1" / "out"
    pdf, dxf = od / "pdf" / f"{no}_Rev{a.rev}.pdf", od / "dxf" / f"{no}_Rev{a.rev}.dxf"
    pdf.parent.mkdir(parents=True, exist_ok=True)
    dxf.parent.mkdir(parents=True, exist_ok=True)
    sh.render_pdf(pdf, title=f"{no} Rev {a.rev} {SHEETS[a.sheet][1].replace(chr(10), ' ')}")
    sh.render_dxf(dxf)
    print(f"wrote {pdf}\nwrote {dxf}")


if __name__ == "__main__":
    main()
