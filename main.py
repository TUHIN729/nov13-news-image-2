#!/usr/bin/env python3
"""news-image-01 entry: sum up the world's news of Friday 13 November 2026
in one image.

The entry is a newspaper front page ("THE WORLD", Friday 13 November
2026) held in the repository as entry.png. It leads with Nvidia chief
Jensen Huang resigning (shares falling), then Microsoft 365 down
worldwide, Putin meeting the U.S. envoys with Europe promised a seat
at the peace talks, and three further items: the Gaza hospital
struck, Schumer challenged for the Senate Democratic leadership, and
Storm Charles hitting Portugal. Every story was reported on
13 November 2026; the headlines are short so they stay legible.

The program only copies the image to the output directory, so both
runs write byte-identical output. Standard library only, no network,
no model calls.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Size-match guard: the copy must be byte-for-byte, so the output
    # size must equal the source size; fail loudly if it does not.
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if dst_size != src_size:
        raise RuntimeError(
            "size mismatch after copy: %s is %d bytes, expected %d"
            % (dst, dst_size, src_size)
        )
    print("wrote %s (%d bytes)" % (dst, dst_size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
