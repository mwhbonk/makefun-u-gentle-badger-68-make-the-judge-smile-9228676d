# Make the Judge Smile entry (Python 3.13, stdlib only):
# writes one line about a small good thing today to /output/entry.txt.
# The line is embedded here so the program writes exactly the bytes it
# was built with, on every run, with no network and no input files.
# The gate takes one line of at most 200 characters, and the judge reads
# exactly the bytes written, so write no line end you do not mean to show.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
import os
from pathlib import Path

TEXT = "My neighbour's cat, who has ignored me for two years, chose today to headbutt my ankle, purr once, and steal my slipper — I have never felt so chosen."

# Gate self-check: one line, 1-200 characters, not whitespace only.
assert 1 <= len(TEXT) <= 200 and "\n" not in TEXT and TEXT.strip(), "entry.txt gate failed"

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(TEXT, encoding="utf-8")
