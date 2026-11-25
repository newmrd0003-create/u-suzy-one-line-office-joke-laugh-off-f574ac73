#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to /output/entry.txt
(and ./entry.txt for local verification). Deterministic: the joke is
hardcoded, no randomness, no network, no external dependencies.
"""

import os

JOKE = "The company preaches transparency, so the meeting rooms are glass and the salary bands are frosted."


def main() -> None:
    for path in ("/output/entry.txt", "entry.txt"):
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(JOKE)


if __name__ == "__main__":
    main()
