import os
from pathlib import Path

TEXT = "In a north-facing room, a glass of water left by the window overnight grows a fern of ice by morning. Eleven winters now, the same fern, a fraction wider each year — as if the cold were learning the room by heart, and in no hurry to finish."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
