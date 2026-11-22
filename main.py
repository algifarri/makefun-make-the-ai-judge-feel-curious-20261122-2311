#!/usr/bin/env python3
"""Make the AI judge feel curious — a short text written to intrigue the AI judge.

Writes the text to /output/entry.txt (UTF-8, 234 Unicode code points,
inside the 1-280 gate). Deterministic, standard library only, no network.

The text itself: an old man plants one seed every morning in the same
bare patch of earth, waters it, and walks home — nothing has ever grown
there, in thirty-one years, and he has never once looked disappointed.
Two open loops (why plant where nothing grows? why no disappointment?),
shown in a calm, concrete scene rather than told — plain words, a slow
rhythm, and an image that keeps working after the last line.
"""

import os

TEXT = (
    "Every morning the old man at the end of the lane plants one seed in "
    "the same bare patch of earth, waters it, and walks home. Nothing has "
    "ever grown there. He has done it for thirty-one years, and he has "
    "never once looked disappointed."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    # TEXT is exactly 234 Unicode code points: inside the 1-280 gate.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
