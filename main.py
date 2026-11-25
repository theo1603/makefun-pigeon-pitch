#!/usr/bin/env python3
"""Pigeon Pitch, One Line — the elevator pitch a city pigeon gives
investors for its startup.

The line: a breadcrumb-delivery startup with a real joke that lands
— delivery apps charge five bucks to move a sandwich three blocks,
we move it for one crumb — plus traction (12,000 rooftops) and a
clear ask ($2M seed), all in the pigeon's own voice: the last mile
with wings. 157 characters, inside the 200-character gate.
"""

import os

LINE = "Delivery apps charge five bucks to move a sandwich three blocks; we move it for one crumb. $2M seed, 12,000 rooftops strong \u2014 we're the last mile with wings."

MAX_CHARS = 200


def output_path() -> str:
    """Write to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def validate(line: str) -> str:
    """Return the line if it passes the gate, else raise with the reason."""
    text = line.strip()
    if not text:
        raise ValueError("line is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    return text


def main() -> None:
    line = validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Atomic write: a crash mid-write never leaves a partial entry behind.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.replace(tmp_path, path)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
