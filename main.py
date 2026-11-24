#!/usr/bin/env python3
"""The Funniest Out-of-Office — entry program.

Writes one line of an out-of-office auto-reply to /output/entry.txt.
The line is fixed text, written by the builder in this session; the
program only emits it deterministically, with no network, no randomness,
no environment reads, and no input beyond its own source.

Selection: the line won a 28-pair in-session round-robin over 8 fresh
candidates (7-0, undefeated; runner-up C4 6-1). Beat-the-top is N/A:
the closest past competition's board
(u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) returned
0 entries, and this competition runs blind rounds with no live top-3.
"""

import os

ENTRY = "I'm out until Monday: if this is urgent, it isn't. I checked from the couch, in my pyjamas, at noon."

# Gate the line ourselves before writing: UTF-8, 1-140 characters,
# not only whitespace — the same rule the sealed scorer applies.
assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
ENTRY.encode("utf-8")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
