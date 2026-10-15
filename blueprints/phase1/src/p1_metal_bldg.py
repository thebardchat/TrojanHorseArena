#!/usr/bin/env python3
"""KEYSTONE Phase 1 ALTERNATE: new pre-engineered metal building (Summertown Metals) on HGHS property, replacing the old wrestling room (D-094).
West half = wrestling mat room, east half = girls' flag football locker room (ASSUMED). All inputs from params/phase1_metal_bldg.yaml.
Sheets (Rev A, 11 x 17, PRELIMINARY): P1-G-101 cover + code summary, P1-A-201 floor plan, P1-A-301 elevations + section, P1-A-901 massing.

  /workspace/.venv-keystone/bin/python blueprints/phase1/src/p1_metal_bldg.py --sheet A-201 --rev A [--out-dir DIR]
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import yaml
from shapely.geometry import Polygon, box
from shapely.ops import unary_union

BP = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BP / "shared"))
from titleblock import Sheet, add_titleblock  # noqa: E402
from palette import SCHOOL_RED, INK_MUTED, MAT, LIGHT_GRAY, TINT_BLUE, TINT_SAND, TINT_GREEN, STEEL  # noqa: E402

P = yaml.safe_load((BP / "params" / "phase1_metal_bldg.yaml").read_text(encoding="utf-8"))
P1 = yaml.safe_load((BP / "params" / "phase1.yaml").read_text(encoding="utf-8"))
W, H = 17.0, 11.0
GRY = INK_MUTED
B = P["building"]
L, D = B["length_ft"]["value"], B["width_ft"]["value"]
EAVE, PITCH = B["eave_ft"]["value"], B["roof_pitch"]["value"] / 12.0
RIDGE = EAVE + D / 2 * PITCH
WT = B["wall_in"]["value"] / 12.0
IT = P["locker_side"]["walls"]["thick_in"] / 12.0
FRAMES = [i * B["bay_ft"]["value"] for i in range(int(L / B["bay_ft"]["value"]) + 1)]
ECOLS = [i * B["endwall_col_ft"]["value"] for i in range(int(D / B["endwall_col_ft"]["value"]) + 1)]
LS = P["locker_side"]
ROOMS = {r["id"]: r for r in LS["rooms"]}
LR = Polygon(LS["locker_room"]["pts"])
WR = box(*P["wrestling"]["rect"])
DOORS = P["doors"]
SHEETS = {
    "G-101": ("P1-G-101", "COVER + CODE SUMMARY\nMETAL BUILDING (ALT.)", "NTS"),
    "A-201": ("P1-A-201", "FLOOR PLAN\nMETAL BUILDING (ALT.)", "1\" = 10'-0\""),
    "A-301": ("P1-A-301", "ELEVATIONS + SECTION\nMETAL BUILDING (ALT.)", "1/16\" = 1'-0\""),
    "A-901": ("P1-A-901", "3D MASSING\nMETAL BUILDING (ALT.)", "NTS"),
}


# ---------------------------------------------------------------- numbers (shared by all sheets)
def occ():
    rows = [("Wrestling mat room", WR.area, P["wrestling"]["occ_factor"]["value"]),
            ("Flag football locker room", LR.area, LS["locker_room"]["factor"])]
    for rid in ("office", "jan", "storage"):
        r = ROOMS[rid]["rect"]
        rows.append((ROOMS[rid]["label"].title(), (r[2] - r[0]) * (r[3] - r[1]), ROOMS[rid]["factor"]))
    out = [(n, a, f, math.ceil(a / f - 1e-9)) for n, a, f in rows]
    return out, sum(o[3] for o in out)


def fixtures(total):
    r = P["fixtures"]["ratios"]
    half = math.ceil(total / 2)
    need = dict(wc_f=math.ceil(half / r["wc_f"]), wc_m=math.ceil(half / r["wc_m"]), lav_f=math.ceil(half / r["lav_f"]),
                lav_m=math.ceil(half / r["lav_m"]), df=math.ceil(total / r["df"]), ss=1)
    return half, need


def exits():
    ex = [d for d in DOORS if d["exit"]]
    pts = {"S": lambda a: (a, 0), "N": lambda a: (a, D), "W": lambda a: (0, a), "E": lambda a: (L, a)}
    ep = [(d["id"], pts[d["wall"]](d["at"])) for d in ex]
    # worst points (manhattan to the nearest exit, routes ASSUMED through the drawn doors)
    worst = {"mat room NW corner": (1, D - 1), "mat room NE corner": (49, D - 1), "toilet / shower far corner": (99, 15),
             "locker room NW": (59, 51), "storage far corner": (99, 1), "coach office": (59, 1)}
    via = {"toilet / shower far corner": [(80, 30), (90, 38)], "storage far corner": [(90, 0)], "coach office": [(58, 7), (54, 0)],
           "locker room NW": [(58, 44), (54, 60)]}
    res = []
    for k, p in worst.items():
        if k in via:
            path = [p] + via[k]
            dist = sum(abs(b[0] - a[0]) + abs(b[1] - a[1]) for a, b in zip(path[:-1], path[1:]))
            last = path[-1]
            e = min(ep, key=lambda q: abs(q[1][0] - last[0]) + abs(q[1][1] - last[1]))
            dist += abs(e[1][0] - last[0]) + abs(e[1][1] - last[1])
        else:
            e = min(ep, key=lambda q: abs(q[1][0] - p[0]) + abs(q[1][1] - p[1]))
            dist = abs(e[1][0] - p[0]) + abs(e[1][1] - p[1])
        res.append((k, e[0], dist))
    return ex, res


OCC, TOTAL = occ()
HALF, NEED = fixtures(TOTAL)
EXITS, TRAVEL = exits()
EX_IN = sum(d["width_in"] for d in EXITS)
NEED_IN = TOTAL * P["code"]["egress_in_per_occ"]["value"]
PV = P["fixtures"]["provided"]
FLAGS = dict(travel=max(t[2] for t in TRAVEL) <= P["code"]["travel_ft"]["value"], width=EX_IN >= NEED_IN,
             wc_f=PV["girls_wc"] >= NEED["wc_f"], wc_m=PV["single_user_wc"] >= NEED["wc_m"],
             lav=PV["girls_lav"] >= NEED["lav_f"] and PV["single_user_lav"] >= NEED["lav_m"], df=PV["df"] >= NEED["df"],
             area=L * D <= 9500, mat_exits=sum(1 for d in DOORS if d["id"] in ("D3", "D4", "I1")) >= 2)


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


# ---------------------------------------------------------------- P1-A-201 floor plan
def plan(sh, ox, oy, s, full=True):
    T = lambda x, y: (ox + x * s, oy + y * s)  # noqa: E731
    R = lambda r, **k: sh.poly([T(r[0], r[1]), T(r[2], r[1]), T(r[2], r[3]), T(r[0], r[3])], **k)  # noqa: E731
    # floor tints
    R(P["wrestling"]["rect"], fill="#EFEFEF", layer="A-FLOR-PATT", lw=0)
    sh.poly([T(x, y) for x, y in LR.exterior.coords], fill=TINT_SAND, layer="A-FLOR-PATT", lw=0)
    R(ROOMS["toilet"]["rect"], fill=TINT_BLUE, layer="A-FLOR-PATT", lw=0)
    R(ROOMS["aguest"]["rect"], fill=TINT_BLUE, layer="A-FLOR-PATT", lw=0)
    R(LS["corridor"]["rect"], fill=TINT_GREEN, layer="A-FLOR-PATT", lw=0)
    # mat + 28 ft circle + wall pads
    m = P["wrestling"]["mat"]["rect"]
    R(m, fill="#C9302C" if full else "#D9534F", layer="A-FLOR-MATS", lw=0.5)
    cx, cy = (m[0] + m[2]) / 2, (m[1] + m[3]) / 2
    sh.poly([T(cx + 14 * math.cos(a / 48 * 2 * math.pi), cy + 14 * math.sin(a / 48 * 2 * math.pi)) for a in range(48)], fill="#E8E8E8", layer="A-FLOR-MATS", lw=0.5)
    sh.poly([T(cx + 5 * math.cos(a / 32 * 2 * math.pi), cy + 5 * math.sin(a / 32 * 2 * math.pi)) for a in range(32)], fill="#C9302C", layer="A-FLOR-MATS", lw=0.4)
    pad = 0.6
    for r in ((WT, WT, 50 - IT / 2, WT + pad), (WT, D - WT - pad, 50 - IT / 2, D - WT), (WT, WT, WT + pad, D - WT), (50 - IT / 2 - pad, WT, 50 - IT / 2, D - WT)):
        R(r, fill="#2B2B2B", layer="A-FLOR-PADS", lw=0)
    # walls (shapely: shell - openings)
    shell = box(0, 0, L, D).difference(box(WT, WT, L - WT, D - WT))
    inner = unary_union([box(min(a, c) - IT / 2, min(b, d) - IT / 2, max(a, c) + IT / 2, max(b, d) + IT / 2) for a, b, c, d in LS["walls"]["list"]])
    walls = shell.union(inner)
    ops = []
    for d_ in DOORS:
        w = d_["width_in"] / 12.0
        if d_["wall"] in ("S", "N"):
            y0 = 0 if d_["wall"] == "S" else D - WT
            ops.append(box(d_["at"] - w / 2, y0 - 0.1, d_["at"] + w / 2, y0 + WT + 0.1))
        elif d_["wall"] in ("W", "E"):
            x0 = 0 if d_["wall"] == "W" else L - WT
            ops.append(box(x0 - 0.1, d_["at"] - w / 2, x0 + WT + 0.1, d_["at"] + w / 2))
        else:
            x = float(d_["wall"][1:])
            ops.append(box(x - IT, d_["at"] - w / 2, x + IT, d_["at"] + w / 2))
    walls = walls.difference(unary_union(ops))
    for g in getattr(walls, "geoms", [walls]):
        sh.poly([T(x, y) for x, y in g.exterior.coords], fill="#1A1A1A", layer="A-WALL", lw=0.3)
        for hole in g.interiors:
            sh.poly([T(x, y) for x, y in hole.coords], fill="#FFFFFF", layer="A-WALL", lw=0.3)
    # door leaves (90 deg swing, outward on exits)
    for d_ in DOORS:
        w = d_["width_in"] / 12.0
        n = 2 if d_["width_in"] >= 60 else 1
        lw_ = w / n
        if d_["wall"] in ("S", "N"):
            sgn = -1 if d_["wall"] == "S" else 1
            yb = 0 if d_["wall"] == "S" else D
            hinges = [(d_["at"] - w / 2, 1)] + ([(d_["at"] + w / 2, -1)] if n == 2 else [])
            for hx, dirn in hinges:
                sh.line(*T(hx, yb), *T(hx, yb + sgn * lw_), layer="A-DOOR", lw=0.5)
                pts = [T(hx + dirn * lw_ * math.sin(a / 12 * math.pi / 2), yb + sgn * lw_ * math.cos(a / 12 * math.pi / 2)) for a in range(13)]
                for p0, p1 in zip(pts[:-1], pts[1:]):
                    sh.line(*p0, *p1, layer="A-DOOR", lw=0.25)
        else:
            if d_["wall"] in ("W", "E"):
                sgn, xb = (-1, 0) if d_["wall"] == "W" else (1, L)
            else:
                xb = float(d_["wall"][1:])
                sgn = 1
            hinges = [(d_["at"] - w / 2, 1)] + ([(d_["at"] + w / 2, -1)] if n == 2 else [])
            for hy, dirn in hinges:
                sh.line(*T(xb, hy), *T(xb + sgn * lw_, hy), layer="A-DOOR", lw=0.5)
                pts = [T(xb + sgn * lw_ * math.cos(a / 12 * math.pi / 2), hy + dirn * lw_ * math.sin(a / 12 * math.pi / 2)) for a in range(13)]
                for p0, p1 in zip(pts[:-1], pts[1:]):
                    sh.line(*p0, *p1, layer="A-DOOR", lw=0.25)
    if not full:
        return T
    # frame grid + bubbles
    for i, x in enumerate(FRAMES):
        sh.dashed(*T(x, -4), *T(x, D + 4), layer="S-GRID", lw=0.3, dash=0.1, gap=0.05)
        bx, by = T(x, D + 6)
        sh.poly([(bx + 0.11 * math.cos(a / 16 * 2 * math.pi), by + 0.11 * math.sin(a / 16 * 2 * math.pi)) for a in range(16)], fill="#FFFFFF", layer="S-GRID", lw=0.4)
        sh.text(bx, by - 0.04, str(i + 1), size=6.5, bold=True, align="center", layer="S-GRID")
        sh.rect(*T(x - 0.6, -0.6), 1.2 * s, 1.2 * s, layer="S-COLS", lw=0.6)
        sh.rect(*T(x - 0.6, D - 0.6), 1.2 * s, 1.2 * s, layer="S-COLS", lw=0.6)
    for j, y in enumerate(ECOLS):
        sh.dashed(*T(-4, y), *T(0, y), layer="S-GRID", lw=0.3, dash=0.1, gap=0.05)
        bx, by = T(-6, y)
        sh.poly([(bx + 0.11 * math.cos(a / 16 * 2 * math.pi), by + 0.11 * math.sin(a / 16 * 2 * math.pi)) for a in range(16)], fill="#FFFFFF", layer="S-GRID", lw=0.4)
        sh.text(bx, by - 0.04, "ABCD"[j], size=6.5, bold=True, align="center", layer="S-GRID")
    # dims
    def dim_h(x0, x1, y, txt):
        sh.line(*T(x0, y), *T(x1, y), layer="A-ANNO-DIMS", lw=0.35)
        for xx in (x0, x1):
            sh.line(*T(xx, y - 0.8), *T(xx, y + 0.8), layer="A-ANNO-DIMS", lw=0.35)
        a, b = T((x0 + x1) / 2, y + 0.8)
        sh.text(a, b, txt, size=6.2, align="center", layer="A-ANNO-DIMS")
    dim_h(0, L, -9, f"{L:g}'-0\" OUT TO OUT (ASSUMED)")
    for x0, x1 in zip(FRAMES[:-1], FRAMES[1:]):
        dim_h(x0, x1, -5.5, f"{x1 - x0:g}'-0\" BAY")
    a, b = T(L + 8, D / 2)
    sh.line(*T(L + 7, 0), *T(L + 7, D), layer="A-ANNO-DIMS", lw=0.35)
    for yy in (0, D):
        sh.line(*T(L + 6.2, yy), *T(L + 7.8, yy), layer="A-ANNO-DIMS", lw=0.35)
    sh.text(a, b, f"{D:g}'-0\" CLEAR SPAN", size=6.2, rot=90, align="center", layer="A-ANNO-DIMS")
    # room tags
    def tag(x, y, t1, t2=None, size=7.2, color=None):
        a, b = T(x, y)
        sh.text(a, b, t1, size=size, bold=True, align="center", layer="A-ANNO-TEXT", color=color)
        if t2:
            sh.text(a, b - 0.15, t2, size=5.6, align="center", layer="A-ANNO-TEXT", color=GRY)
    o = {n: (a, oc) for n, a, f, oc in OCC}
    tag(25, 55.2, "WRESTLING MAT ROOM", f"{WR.area:,.0f} SF · {o['Wrestling mat room'][1]} occ. (50 gross)", size=8)
    tag(25, 4.0, f"42' x 42' MAT · 28' CIRCLE (NFHS 2-1-2)", "6' wall pads all walls · LED high-bay")
    tag(54, 30.5, "CORR.", None, size=6)
    tag(54, 27.5, "8'", None, size=5.6)
    tag(72, 45.5, "FLAG FOOTBALL", None)
    tag(72, 43.6, "LOCKER ROOM", f"{LR.area:,.0f} SF · {o['Flag football locker room'][1]} occ. · girls' (ASSUMED)")
    tag(90, 49.5, "TEAM AREA", "film / board wall", size=6.4)
    rt = ROOMS
    for rid, txt in (("office", "COACH OFFICE"), ("jan", "JAN./MECH"), ("storage", "STORAGE"), ("toilet", "TOILET / SHOWER")):
        r = rt[rid]["rect"]
        ar = (r[2] - r[0]) * (r[3] - r[1])
        tag((r[0] + r[2]) / 2, (r[1] + r[3]) / 2 + (6 if rid == "toilet" else 1.5), txt, f"{ar:,.0f} SF", size=6.4 if rid != "jan" else 5.4)
    r = rt["aguest"]["rect"]
    tag((r[0] + r[2]) / 2, (r[1] + r[3]) / 2 + 0.6, "ACC.", "WC", size=5.4)
    # lockers + benches
    for x0, y0, x1, y1 in ((66.5, 58.75, 100 - WT, 60 - WT), (58 + IT / 2, 15, 59.25 + IT / 2, 40)):
        R((x0, y0, x1, y1), fill="#9AA5B1", layer="A-FURN", lw=0.3)
        n = int(round((x1 - x0 if x1 - x0 > y1 - y0 else y1 - y0) / 1.5))
        for k in range(1, n):
            if x1 - x0 > y1 - y0:
                xx = x0 + k * (x1 - x0) / n
                sh.line(*T(xx, y0), *T(xx, y1), layer="A-FURN", lw=0.15)
            else:
                yy = y0 + k * (y1 - y0) / n
                sh.line(*T(x0, yy), *T(x1, yy), layer="A-FURN", lw=0.15)
    a, b = T(83, 57.2)
    sh.text(a, b, f"LOCKERS 18\" x 15\" — {P['team']['roster']['value']} + {P['team']['accessible_lockers']['value']} ACC. (ASSUMED)", size=5.2, align="center", layer="A-FURN")
    for bx0, by0, bx1, by1 in ((63, 20, 64.75, 32), (67, 20, 68.75, 32), (84, 42, 96, 43.75), (84, 46, 96, 47.75)):
        R((bx0, by0, bx1, by1), fill="#D2B48C", layer="A-FURN", lw=0.3)
    a, b = T(66, 18.2)
    sh.text(a, b, "BENCHES (1 ACC., ADA 903)", size=5.0, align="center", layer="A-FURN", color=GRY)
    # toilet / shower fixtures
    for i in range(3):
        x0 = 80 + IT / 2 + 0.2 + i * 3.4 if i < 2 else 80 + IT / 2 + 7.2
        w_ = 3.0 if i < 2 else 5.2
        R((x0, 14 + IT / 2, x0 + w_, 14 + IT / 2 + (5.0 if i < 2 else 5.2)), fill="#FFFFFF", layer="P-FIXT", lw=0.4)
        a, b = T(x0 + w_ / 2, 16.2)
        sh.text(a, b, "WC" if i < 2 else "ACC WC", size=4.6, align="center", layer="P-FIXT")
    for i in range(4):
        y0 = 15 + IT / 2 + i * 3.6 if i < 3 else 26.2
        R((100 - WT - 3.0 - (2 if i == 3 else 0), y0, 100 - WT, y0 + (3.0 if i < 3 else 5.0)), fill="#DCEBF7", layer="P-FIXT", lw=0.4)
        a, b = T(100 - WT - 1.5 - (1 if i == 3 else 0), y0 + 1.2)
        sh.text(a, b, "SH" if i < 3 else "ACC SH", size=4.4, align="center", layer="P-FIXT")
    for i in range(2):
        R((81 + i * 3, 36.4 - IT / 2, 83 + i * 3, 38 - IT / 2), fill="#FFFFFF", layer="P-FIXT", lw=0.4)
    a, b = T(84, 35.4)
    sh.text(a, b, "LAV x2", size=4.6, align="center", layer="P-FIXT")
    a, b = T(88, 25.5)
    sh.text(a, b, "60\" TURN", size=4.4, align="center", layer="P-FIXT", color=GRY)
    sh.poly([T(88 + 2.5 * math.cos(a / 24 * 2 * math.pi), 26.2 + 2.5 * math.sin(a / 24 * 2 * math.pi)) for a in range(24)], fill=None, layer="P-FIXT", lw=0.25)
    R((50 + IT / 2 + 0.1, 20, 51.4, 23.5), fill="#FFFFFF", layer="P-FIXT", lw=0.4)
    a, b = T(52.6, 21.3)
    sh.text(a, b, "DF hi-lo", size=4.6, layer="P-FIXT")
    # door + exit tags
    for d_ in DOORS:
        if d_["wall"] == "S":
            p = (d_["at"], -2.6)
        elif d_["wall"] == "N":
            p = (d_["at"], D + 1.6)
        elif d_["wall"] == "W":
            p = (-2.4, d_["at"] + 2.6)
        elif d_["wall"] == "E":
            p = (L + 2.4, d_["at"] + 2.6)
        else:
            continue
        a, b = T(*p)
        sh.text(a, b, d_["id"] + (" EXIT" if d_["exit"] else ""), size=5.6, bold=True, align="center", layer="A-ANNO-EXIT", color=SCHOOL_RED if d_["exit"] else None)
    # north arrow
    a, b = T(L + 14, D - 2)
    sh.poly([(a, b + 0.32), (a - 0.1, b), (a + 0.1, b)], fill="#1A1A1A", layer="A-ANNO-TEXT", lw=0.3)
    sh.text(a, b - 0.17, "N", size=8, bold=True, align="center", layer="A-ANNO-TEXT")
    return T


def sheet_a201():
    sh = Sheet(W, H)
    bb = tb(sh, "A-201")
    s, ox, oy = 0.1, 1.15, bb + 1.42
    plan(sh, ox, oy, s)
    sh.text(ox, oy - 1.12, "FLOOR PLAN — NEW METAL TRAINING BUILDING (ALTERNATE)", size=11, bold=True)
    sh.text(ox, oy - 1.28, f"1\" = 10'-0\" · {L:g}' x {D:g}' = {L * D:,.0f} SF clear-span PEMB, 4 x 25' bays (ASSUMED) · plan north up", size=7, color=GRY)
    x, w = 12.75, 3.9
    sh.line(x - 0.12, H - 0.6, x - 0.12, bb + 0.1, lw=0.4)
    y = H - 0.75
    sh.text(x, y, "PLAN NOTES", size=9, bold=True)
    y -= 0.1
    y = note_col(sh, x, y, w, [
        "D-094 (Shane 2026-10-14 9:52 PM CT): new pre-engineered metal building (Summertown Metals) replaces the old 55' x 45' room. West = mat room, east = flag football locker room.",
        f"Size: the 60' x 80' alternate grown to {L:g}' x {D:g}' (ASSUMED) so the locker side holds toilets / showers, office and storage without shrinking the mat room.",
        "Clear-span rigid frames on lines 1-5 @ 25'; endwall columns @ 20' (A-D). Demising wall on line 3 (frame line). No interior columns.",
        f"Mat room: one 42' x 42' mat (28' circle + 7' each side; NFHS 2-1-2 needs >= 5'). 4' E / W, 9' N / S to the walls; 6' wall pads all walls. Clear {B['clear_ft']['value']:g}' min (ASSUMED).",
        f"Locker room: girls' flag football (ASSUMED), {P['team']['roster']['value']} lockers + {P['team']['accessible_lockers']['value']} accessible (ADA 222.1, 811), benches (ADA 903), team / film area.",
        f"Toilet / shower: {PV['girls_wc']} WC (1 acc.), {PV['girls_lav']} lav, {PV['showers']} showers (1 acc. roll-in). All-gender accessible single-user toilet off the corridor. DF hi-lo, service sink in JAN. (counts ASSUMED; G-101).",
        "Exits (red): D1 main pair, D2 north, D3 west, D4 mat-room pair, D5 east. Mat room ({} occ.) has 3 ways out (D3, D4, corridor I1).".format(OCC[0][3]),
        "Accessibility: accessible route at grade, 60\" turning spaces, 36\" doors min; final ADA layout by the architect.",
        "Wall / interior: insulated metal panels (Summertown kit), 6\" interior walls; wet walls TBD (CMU or moisture-resistant). Finishes TBD.",
        "No prices on this set: cost TBD per the Summertown Metals quote, plus site, foundation, MEP, permit and design (not included).",
    ], size=6.6)
    y -= 0.08
    sh.text(x, y, "LEGEND", size=8, bold=True)
    y -= 0.2
    for col, t in (("#C9302C", "wrestling mat (42' x 42')"), ("#2B2B2B", "6' wall pads"), (TINT_SAND, "locker room"), (TINT_BLUE, "toilet / shower"), (TINT_GREEN, "corridor / entry"), ("#9AA5B1", "lockers")):
        sh.poly([(x, y), (x + 0.25, y), (x + 0.25, y + 0.13), (x, y + 0.13)], fill=col, lw=0.3)
        sh.text(x + 0.35, y + 0.02, t, size=6.2)
        y -= 0.2
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
    if face == "S":                                   # office window
        sh.poly([T(62, 4), T(68, 4), T(68, 8), T(62, 8)], fill="#BFD7EA", layer="A-ELEV-GLAZ", lw=0.5)
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
              ("EAST ELEVATION (LOCKER END)", "E", 9.0, top - 1.75), ("WEST ELEVATION (MAT ROOM END)", "W", 9.0, top - 3.55)]
    for t, f, x, y in blocks:
        elev(sh, x, y, s, f)
        sh.text(x, y - 0.32, f"{t} — 1/16\" = 1'-0\"", size=7.6, bold=True)
    section(sh, 0.9 + 0.2, top - 6.35, s * 1.6)
    sh.text(0.9, top - 6.75, "SECTION A-A THROUGH THE MAT ROOM (looking west) — 1/10\" = 1'-0\"", size=7.6, bold=True)
    x, w = 9.0, 7.4
    y = top - 4.25
    sh.line(x - 0.15, y + 0.15, x - 0.15, bb + 0.1, lw=0.4)
    sh.text(x, y, "NOTES", size=9, bold=True)
    y = note_col(sh, x, y - 0.1, w, [
        f"Pre-engineered clear-span rigid frame, 1:12 gable (ASSUMED). Eave {EAVE:g}' (ASSUMED), ridge {RIDGE:.2f}' computed from the pitch. Final frame, eave and clear height by Summertown Metals' engineer.",
        "Walls / roof: insulated metal panels (IMP or metal + liner, Summertown kit), R-values per the Alabama Energy Code (IECC 2015 / 90.1-2013) — TBD by supplier (R-028.4).",
        "Daylight: translucent wall-panel band 12'-14' (ASSUMED) on all faces; skylights only where code / supplier allow (D-093 direction). LED high-bay in the mat room; LED elsewhere.",
        "Color: crimson wainscot 0-3' (school color, ASSUMED); light gray panels; dark roof (ASSUMED). Gutters / downspouts to rain capture if the campus wants it (unsized).",
        "Doors: hollow-metal exit doors with panic hardware on D1-D5 (Group A, IBC 1010.2.9); D7 storage pair (not an exit). Red tags = exits.",
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
    Pf = massing(sh, 2.2, bb + 1.9 + 50 * 0.5 * 0.05, 0.05, "SE")
    sh.text(0.8, top, "V1  AERIAL FROM THE SOUTHEAST (main entry + locker end)", size=9, bold=True)
    sh.text(0.8, top - 0.18, "isometric · not to scale · massing only", size=6.4, color=GRY)
    for (x, y, z), dx, dy, t in (((25, 0, 8), -0.4, -0.8, "MAT ROOM (west half) — D3 / D4 exits"), ((54, -6, 9), -0.5, -1.0, "D1 MAIN ENTRY + canopy (ASSUMED)"),
                                 ((L, 50, 6), 0.6, -0.3, "LOCKER END — D5 exit"), ((50, D / 2, RIDGE), 0.2, 0.7, f"1:12 gable, ridge {RIDGE:.2f}' (ASSUMED)"),
                                 ((70, 0, 13), 1.9, -0.25, "translucent daylight band 12'-14' (ASSUMED)"), ((88, 0, 1.5), 1.3, -0.25, "crimson wainscot 0-3' (ASSUMED)")):
        a, b = Pf(x, y, z)
        sh.line(a, b, a + dx, b + dy, lw=0.35)
        sh.text(a + dx + (0.04 if dx > 0 else -0.04), b + dy - 0.03, t, size=6.0, align="left" if dx > 0 else "right")
    massing(sh, 11.5, bb + 4.9 + 50 * 0.5 * 0.034, 0.034, "NW")
    sh.text(11.4, top, "V2  FROM THE NORTHWEST (mat room end, D2 / D3)", size=8, bold=True)
    x, w = 11.4, 5.0
    y = bb + 3.7
    sh.text(x, y, "NOTES", size=9, bold=True)
    y = note_col(sh, x, y - 0.1, w, [
        f"Massing only: {L:g}' x {D:g}' x {EAVE:g}' eave pre-engineered metal building (ASSUMED sizes) from params/phase1_metal_bldg.yaml.",
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
    sh.text(x0, y - 0.38, "New metal training building — PROPOSAL SET REV A", size=9.5, bold=True)
    y = sh.para(x0, y - 0.62, 5.4, f"Replaces the old 55' x 45' wrestling room (10' ceiling) at Hazel Green High School, 14380 Hwy 231-431 N, Hazel Green, AL 35750 (Madison County Schools property; location on campus TBD). Supplier: {P['supplier']['name']}, {P['supplier']['address']}, {P['supplier']['phone']} (quote TBD).", size=7.4)
    y -= 0.1
    sh.text(x0, y, "SHEET INDEX", size=9, bold=True)
    y -= 0.22
    for no, t in (("P1-G-101", "Cover + code summary"), ("P1-A-201", "Floor plan"), ("P1-A-301", "Elevations + section"), ("P1-A-901", "3D massing")):
        sh.text(x0, y, no, size=7.4, bold=True)
        sh.text(x0 + 1.0, y, t + " — Rev A", size=7.4)
        y -= 0.19
    y -= 0.08
    sh.text(x0, y, "PROJECT DATA (ASSUMED unless cited)", size=9, bold=True)
    y -= 0.08
    y = note_col(sh, x0, y, 5.4, [
        f"Building {L:g}' x {D:g}' = {L * D:,.0f} SF, 1 storey, clear span, 4 x 25' bays, eave {EAVE:g}', {B['clear_ft']['value']:g}' min clear, 1:12 gable.",
        f"West: wrestling mat room {WR.area:,.0f} SF, one 42' x 42' mat. East: girls' flag football locker room {LR.area:,.0f} SF + toilet / shower, coach office, storage, JAN. / mech, corridor.",
        "D-094 (Shane 2026-10-14 9:52 PM CT): proposal set for the new building; the remodel (P1-G-001 Rev E, P1-A-101 Rev C, P1-G-002 Rev B) stays the base option.",
        "Cost: TBD per the Summertown Metals quote + site, foundation, MEP, permit, design. No prices invented. Companion text proposal (Shane, 2026-10-14) carries the remodel figures.",
        "Contact: Shane Brazelton, 256-508-4608, brazeltonshane@gmail.com.",
    ], size=7.0)
    # code summary column
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
        sh.text(cx + 3.0, y, f"{a:,.0f} SF / {f}", size=6.6, align="right")
        sh.text(cx + 3.9, y, f"{oc}", size=6.6, align="right")
        y -= 0.17
    sh.text(cx, y, "TOTAL (toilets / corridor accessory)", size=6.6, bold=True)
    sh.text(cx + 3.9, y, f"{TOTAL}", size=6.6, bold=True, align="right")
    y -= 0.27
    sh.text(cx, y, "EGRESS", size=7.6, bold=True)
    y -= 0.08
    wt = max(TRAVEL, key=lambda t: t[2])
    y = note_col(sh, cx, y, 4.9, [
        f"Width: {TOTAL} x {c['egress_in_per_occ']['value']} in = {NEED_IN:.1f} in needed (1005.3.2) vs {EX_IN} in of exit doors (D1-D5): {'PASS' if FLAGS['width'] else 'CHECK'}.",
        f"Mat room {OCC[0][3]} occ. > 49: 2 exits needed (1006.2.1); 3 provided (D3, D4, corridor): {'PASS' if FLAGS['mat_exits'] else 'CHECK'}. Locker room {OCC[1][3]} occ.: 1 needed, D5 + corridor.",
        f"Travel (Table 1017.2, {c['travel_ft']['value']} ft non-sprinklered): worst {wt[2]:.0f} ft ({wt[0]} to {wt[1]}, routes ASSUMED): {'PASS' if FLAGS['travel'] else 'CHECK'}.",
        "Exit doors: panic hardware (1010.2.9); exit signs + egress lighting (1008, 1013).",
    ], size=6.6)
    # fixtures column
    fx = 11.85
    sh.line(fx - 0.15, H - 0.6, fx - 0.15, bb + 0.1, lw=0.4)
    y = H - 0.75
    sh.text(fx, y, "PLUMBING FIXTURES — IPC 2021 Table 2902.1", size=9, bold=True)
    y -= 0.08
    y = sh.para(fx, y, 4.6, f"Basis: {P['fixtures']['basis']['text']} (ASSUMED). {TOTAL} occ. -> {HALF} F + {HALF} M.", size=6.6) - 0.08
    r = P["fixtures"]["ratios"]
    rows = [("WC — female", f"1:{r['wc_f']}", NEED["wc_f"], f"{PV['girls_wc']} (1 acc.)", FLAGS["wc_f"]),
            ("WC — male", f"1:{r['wc_m']}", NEED["wc_m"], f"{PV['single_user_wc']} single-user*", FLAGS["wc_m"]),
            ("Lavatory", f"1:{r['lav_f']} F / 1:{r['lav_m']} M", NEED["lav_f"] + NEED["lav_m"], f"{PV['girls_lav'] + PV['single_user_lav']}", FLAGS["lav"]),
            ("Drinking fountain", f"1:{r['df']}", NEED["df"], f"{PV['df']} (hi-lo)", FLAGS["df"]),
            ("Service sink", "1", NEED["ss"], f"{PV['service_sink']} (JAN.)", True),
            ("Showers", "not required (A-3)", 0, f"{PV['showers']} (1 acc. roll-in)", True)]
    for t in (("FIXTURE", 0), ("RATIO", 1.25), ("REQ.", 2.7), ("PROVIDED", 3.15)):
        sh.text(fx + t[1], y, t[0], size=6.2, bold=True)
    y -= 0.18
    for n, rr, req, prov, ok in rows:
        sh.text(fx, y, n, size=6.3)
        sh.text(fx + 1.25, y, rr, size=6.3)
        sh.text(fx + 2.8, y, str(req), size=6.3)
        sh.text(fx + 3.15, y, prov + (" PASS" if ok else " CHECK"), size=6.3)
        y -= 0.17
    y = sh.para(fx, y - 0.03, 4.6, "* single-user all-gender accessible toilet counted toward the male fixtures (IPC 2902.1.2) — AHJ to confirm. Boys' wrestling uses the existing HGHS locker rooms (ASSUMED).", size=6.0) - 0.1
    sh.text(fx, y, "OPEN ITEMS / FINDINGS", size=8, bold=True, color=SCHOOL_RED)
    y -= 0.08
    y = note_col(sh, fx, y, 4.6, [
        "Size 60' x 100' vs the 60' x 80' alternate: Shane to confirm (80' shrinks the locker side to 30').",
        "Team: girls' flag football + roster 30 ASSUMED; confirm with HGHS athletics.",
        "Location on campus, utilities (water / sewer for showers), geotech: TBD with Madison County Schools.",
        "Sprinklers / fire alarm: AHJ + district policy. Energy code envelope: supplier.",
        "Supplier quote: Summertown Metals (kit only); everything else TBD.",
    ], size=6.4)
    if y < bb + 0.1:
        raise SystemExit("LAYOUT OVERFLOW: G-101")
    return sh


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", choices=list(SHEETS), required=True)
    ap.add_argument("--rev", choices=["A"], required=True)
    ap.add_argument("--out-dir")
    ap.add_argument("--print", action="store_true")
    a = ap.parse_args()
    if a.print:
        print(OCC, TOTAL, NEED, EX_IN, NEED_IN, TRAVEL, FLAGS)
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
