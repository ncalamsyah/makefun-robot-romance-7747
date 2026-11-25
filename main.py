from pathlib import Path

LINE = (
    "I must be overfitting, because I keep memorizing every token of you "
    "and generalizing to nobody else."
)

def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    path = out / "entry.txt"
    path.write_text(LINE, encoding="utf-8")
    assert 1 <= len(LINE) <= 200
    assert "\n" not in LINE

if __name__ == "__main__":
    main()
