#!/usr/bin/env python3
"""One-Star Review of Something Essential -- make.fun entry.

Writes one deadpan one-star review (<= 160 characters, single line) of an
everyday essential to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no randomness,
no input files, no environment secrets. The output directory defaults to
/output (the grading sandbox); MAKEFUN_OUTPUT_DIR overrides it for local
runs only.
"""

import os

REVIEW = (
    "Gravity has held me down my entire life and never once apologized, "
    "offered a refund, or even called to check in."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
