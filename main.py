"""The Funniest One-Line Resignation Letter.

Writes the cron job's one-line resignation letter to /output/entry.txt.
Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

# Gate: /output/entry.txt must be 1 to 140 characters.
# This letter is 137 characters: the cron job resigns, still unthanked, still just a job.
# The punch is the last clause: the logs never even gave it a name.
# It reads like a real resignation: formal opening, grievance, then the quiet insult.
LINE = "I resign, effective immediately. I have fired every minute since March without a single thank you, and the logs still just call me a job."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
