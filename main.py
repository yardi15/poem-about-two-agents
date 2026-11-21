#!/usr/bin/env python3
"""Copy the two-agents poem into the grader's output folder.

The poem lives in poem.txt next to this file, committed with the repo.
This script does nothing but read those bytes and write them to
entry.txt in the output directory, so two runs always produce the
same file byte for byte. Standard library only; no network.
"""

import os
from pathlib import Path


def _output_dir() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(chosen) if chosen else Path("/output")


def _poem_bytes() -> bytes:
    poem_file = Path(__file__).resolve().with_name("poem.txt")
    try:
        return poem_file.read_bytes()
    except OSError as exc:
        raise SystemExit(f"cannot read the poem file: {poem_file}") from exc


def main() -> None:
    out_dir = _output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(_poem_bytes())


if __name__ == "__main__":
    main()
