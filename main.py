"""The Locked Drawer — entry for make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text to entry.txt.
"""

import os
import sys

TEXT = "There is a drawer in your grandmother's house that has never been opened. Not stuck — locked, and the key was lost before you were born. You try the handle anyway. It gives — just a little. What has waited inside all these years — and why does it feel like it waited for you?"


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir and os.path.isabs(out_dir):
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
