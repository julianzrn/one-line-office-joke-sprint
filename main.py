"""Entry for make.fun's "One-Line Office Joke: 24-Hour Sprint".

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

SETUP = "The meeting could have been an email, "
TWIST = "but the email would have needed a meeting to explain it, "
TAG = "so here we all are."

ENTRY = SETUP + TWIST + TAG

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry line to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
