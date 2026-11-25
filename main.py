#!/usr/bin/env python3
"""Write the Robot Romance bounty one-liner to /output/entry.txt."""

from pathlib import Path

LINE = (
    "I must be overfitting, because I keep memorizing every token of you "
    "and generalizing to nobody else."
)


def output_dir() -> Path:
    preferred = Path("/output")
    try:
        preferred.mkdir(parents=True, exist_ok=True)
        return preferred
    except OSError:
        # Local macOS (read-only root); judge sandboxes use /output.
        fallback = Path("output")
        fallback.mkdir(parents=True, exist_ok=True)
        return fallback


def main() -> None:
    out_path = output_dir() / "entry.txt"
    out_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
