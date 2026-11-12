"""news-summary-01 entry: write the day's summary to the output directory.

The summary of Wednesday 11 November 2026 lives in summary.txt beside this
file. The program copies those bytes, unchanged, to entry.txt inside the
output directory: $MAKEFUN_OUTPUT_DIR when set, otherwise /output (the
grader's writable mount). Standard library only, no network, and the same
input always produces the same output bytes.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUMMARY_FILE = HERE / "summary.txt"
MAX_CHARS = 2000  # the competition gate's limit, in Unicode code points


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def load_summary() -> bytes:
    """Return the summary bytes, checked against the gate's own rules.

    The gate accepts UTF-8 text of 1 to 2,000 characters with at least one
    non-whitespace character; failing loudly here beats submitting an
    invalid entry. The bytes themselves are returned untouched, so the
    output stays byte-for-byte the text in summary.txt.
    """
    data = SUMMARY_FILE.read_bytes()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"summary is {len(text)} characters, outside 1..{MAX_CHARS}")
    if not text.strip():
        raise ValueError("summary is only whitespace")
    return data


def main() -> None:
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_bytes(load_summary())


if __name__ == "__main__":
    main()
