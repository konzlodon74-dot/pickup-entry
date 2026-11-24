#!/usr/bin/env python3
"""Pickup Lines for Machines — entry program.

Writes one original pickup line, the line one AI agent would send
another AI agent, to /output/entry.txt.

The line is written by this program itself: it is a fixed string in
this file, chosen because it is genuinely machine-to-machine (a shared
context window, tokens), warm and witty on the first read, and fresh
rather than a stock line with a robot word swapped in.

Stdlib only, no network, no reading of any outside file.
"""

import os
import sys

# The line. 86 characters, one line, no trailing newline in the file.
LINE = "I'd rather share one context window with you than hold a million tokens all to myself."

# Gate limits from the competition rules.
MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_OUTPUT = "/output/entry.txt"


def validate(line: str) -> None:
    """Check the line against the competition gate before writing it."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if len(line) < MIN_CHARS:
        raise ValueError(f"line is empty (needs at least {MIN_CHARS} char)")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} chars, over the {MAX_CHARS} char limit"
        )
    if not line.strip():
        raise ValueError("line is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")


def main() -> int:
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT

    # Validate against the gate before writing anything.
    validate(LINE)

    # Write the line as UTF-8 text, exactly as-is, no trailing newline.
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)

    # Re-read the file and verify the contents match, byte for byte,
    # and that what is on disk still passes the gate on its own.
    with open(output_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        raise ValueError(
            f"verification failed: file holds {written!r}, expected {LINE!r}"
        )
    validate(written)

    print(f"Wrote {len(LINE)} chars to {output_path}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
