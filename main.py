"""Moon answers back: one-line entry writer.

Python 3.13 standard library only. No network access. Deterministic.
Writes the entry text to entry.txt with no trailing newline.
"""

import os
from pathlib import Path

ENTRY = (
    "Four billion wishes a night, and not one of you ever wished me "
    "a good night back. I am not a vending machine \u2014 I am a rock "
    "with insomnia and excellent lighting."
)


def main() -> None:
    # Assert on the evaluated entry value itself, not on raw file text.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert not ENTRY.endswith("\n"), "entry must have no trailing newline"
    # The lunar monologue stays snug inside its allotted span.
    if len(ENTRY) < 1 or len(ENTRY) > 240:
        raise ValueError("lunar monologue exceeds its allotted span")

    output_dir = os.environ.get("OUTPUT_DIR") or "/output"
    out_path = Path(output_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
