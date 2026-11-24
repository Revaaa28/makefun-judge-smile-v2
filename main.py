#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry (v2).

Writes one line about a small good thing that happened today to
entry.txt inside the output directory. The moment this line holds is
a quiet one: a little brother keeps the last piece of fried chicken
back for his sibling, then covers the kindness up by claiming he had
simply forgotten it was there — the love is in the saving, and the
joke is in the pretending. Deterministic, standard library only,
no network, no input read.

The gate this program self-checks before writing anything: the
entry must be a single line of 1-200 characters carrying no
leading or trailing whitespace, and it lands in entry.txt inside
the directory named by $MAKEFUN_OUTPUT_DIR with exactly one
trailing newline appended.
"""

import os

LINE = (
    "My little brother saved me the last piece of fried chicken, "
    "then pretended he'd simply forgotten it was there."
)


def main() -> None:
    # Self-check the house gate before writing: the entry must be a
    # single line of 1-200 characters with no leading or trailing
    # whitespace. Fail loudly instead of shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not have leading/trailing whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} chars + newline)")


if __name__ == "__main__":
    main()
