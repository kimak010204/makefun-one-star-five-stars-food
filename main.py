#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single sentence (at most 200 characters) to /output/entry.txt:
a one-star review of Earth by an alien tourist that still slips in a
real compliment about the food.
"""

import os

ENTRY = (
    "One star: the moon stalked me all week, the rain has no off switch, "
    "and humans queue for fun \u2014 but the bakso broth alone made me "
    "rebook the abduction."
)


def main() -> None:
    # Gate, same as the sealed scorer: UTF-8 text, 1 to 200 characters,
    # not only white space, exactly one sentence on one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    assert ENTRY.count(".") == 1 and ENTRY.endswith(".")
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "output", "entry.txt")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    print(ENTRY)
    print("chars:", len(ENTRY))


if __name__ == "__main__":
    main()
