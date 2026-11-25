#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes one sentence (<= 240 chars) pitching the worst, most useless app
imaginable to /output/entry.txt. Pure stdlib, no network, no files read.
"""

import os

PITCH = (
    "SockPair uses AI to photograph the socks you still own and confidently "
    "reports that your missing sock was last seen inside the dryer you "
    "already checked twice, so you can stop searching and start accepting "
    "the loss."
)


def main() -> None:
    assert 1 <= len(PITCH) <= 240, f"pitch is {len(PITCH)} chars"
    assert PITCH.strip() == PITCH and PITCH.strip()
    # The gate reads the file as UTF-8 text of 1-240 chars: reject any
    # control character or newline here so a bad pitch fails loudly
    # instead of shipping an invalid entry.
    assert all(ord(c) >= 0x20 for c in PITCH), "pitch has control chars"
    assert PITCH.encode("utf-8").decode("utf-8") == PITCH
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
