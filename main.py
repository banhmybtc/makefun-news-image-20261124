#!/usr/bin/env python3
"""make.fun entry: news-image-20261124.

Copies the pre-rendered front-page image (entry.png, shipped in this
repository) to $MAKEFUN_OUTPUT_DIR/entry.png, byte for byte.
Python 3.13, standard library only, no network, deterministic: both
grading runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))


if __name__ == "__main__":
    main()
