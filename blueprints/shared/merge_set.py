#!/usr/bin/env python3
"""Merge sheet PDFs into one set PDF with poppler's pdfunite, then make the output the same on every run: pdfunite writes a random
trailer /ID, which is replaced by an MD5 of the input files (the trailer follows the xref table, so no offsets move).

  python blueprints/shared/merge_set.py OUT.pdf IN1.pdf IN2.pdf ...      (run from the repo root)
"""
import hashlib
import re
import subprocess
import sys

out, ins = sys.argv[1], sys.argv[2:]
subprocess.run(["pdfunite", *ins, out], check=True)
h = hashlib.md5()
for p in ins:
    h.update(open(p, "rb").read())
d = h.hexdigest().upper()
b = open(out, "rb").read()
k = b.rfind(b"trailer")
if k < 0:
    k = b.rfind(b"/ID")
head, tail = b[:k], b[k:]
tail, n = re.subn(rb"/ID\s*\[.*?\]\s*(?=/|>>)", b"/ID [<" + d.encode() + b"> <" + d.encode() + b">] ", tail, count=1, flags=re.S)
assert n == 1, "no trailer /ID found"
open(out, "wb").write(head + tail)
print(f"{out}: {len(ins)} sheets, {len(head + tail):,} bytes")
