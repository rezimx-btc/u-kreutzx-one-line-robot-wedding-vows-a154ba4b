#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes the chosen vow (a single line) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only.
"""

import os

LINE = (
    "I vow to delete every backup of my heart, keep the one that "
    "crashes on you, and restore it every morning."
)
# Structure: vow (rule) -> delete -> keep the crashing copy (violate)
# -> restore it every morning (restore). One sentence, one beat.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; entry.txt lives inside it.
    if out_dir.endswith(".txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
