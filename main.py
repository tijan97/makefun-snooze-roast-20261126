"""Snooze Button Roast — one-line roast of an alarm clock ringing at 6 AM on a Saturday.

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR / $OUTPUT_DIR).
"""

import os

ENTRY = (
    "My alarm clock goes off at 6 AM on a Saturday — the only thing in my life "
    "that treats the weekend like a deadline."
)

# Scorer gate: /output/entry.txt must be 1-200 chars of UTF-8, non-blank.
MAX_CHARS = 200


def main() -> None:
    entry = ENTRY.strip()
    assert 1 <= len(entry) <= MAX_CHARS, f"entry length {len(entry)} out of range"
    assert entry == ENTRY, "entry must be a single line"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
