"""Re-spaced colonnade (D-090; params/phase2_colonnade_rev_b.yaml). No sheet output. apply(fz) rewrites a loaded phase2_facade_srm.yaml dict
so x0 / x1 are the end columns and columns_x lists the centres (symmetric about the open entry centre line)."""
import os

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
CB = yaml.safe_load(open(os.path.join(HERE, "..", "..", "params", "phase2_colonnade_rev_b.yaml"), encoding="utf-8"))
CX = CB["centre_x"]["value"]
D = CB["column_dia_ft"]["value"]
INNER = CB["centre_bay_clear_ft"]["value"] / 2 + D / 2          # centre line to an inner column centre
COLS = []
for k in range(CB["per_side"]["value"]):
    off = INNER + k * CB["side_bay_ft"]["value"]
    COLS += [CX - off, CX + off]
COLS = sorted(round(c, 3) for c in COLS)
CENTRE_BAY_CC = 2 * INNER
assert not any(abs(c - CX) < 1e-6 for c in COLS)


def apply(fz):
    co = fz["colonnade"]
    co["x0"], co["x1"] = COLS[0], COLS[-1]
    co["columns_x"] = list(COLS)
    co["basis"] = "D-090: symmetric about x 113 (entry / portal centre line OPEN), centre bay %.1f ft c-c, side bays %.1f ft (ASSUMED)" % (CENTRE_BAY_CC, CB["side_bay_ft"]["value"])
    return fz


if __name__ == "__main__":
    print(COLS, CENTRE_BAY_CC)
