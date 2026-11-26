"""Write the entry number for make.fun's "How Many Tabs Do You Have
Open?" bounty.

One number, digits only, at most 5 characters: the honest count of open
browser tabs. The count is 404, which is also exactly how findable any
one of those tabs is. The program writes the number to entry.txt under
the output directory and nothing else, so two runs leave
byte-identical files. It uses only the standard library and never
touches the network.
"""

import os
import sys
from pathlib import Path

COUNT = "404"

MIN_CHARS = 1
MAX_CHARS = 5


def write_entry() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = output_dir / "entry.txt"
    if not MIN_CHARS <= len(COUNT) <= MAX_CHARS:
        sys.exit("count must be 1 to 5 characters")
    if not COUNT.isdigit():
        sys.exit("count must be digits only")
    output_dir.mkdir(parents=True, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would raise PermissionError and fail the run.
    target.write_text(COUNT, encoding="utf-8")
    try:
        target.chmod(0o644)
    except PermissionError:
        pass
    return target


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written} ({COUNT} tabs open)")
