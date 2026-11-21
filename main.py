"""Write the poem about permission to /output/entry.txt.

The entry is a short poem about agency: a key the speaker did not
make, a lock that answers in someone else's voice, and the weight of
being let through a door that opens on someone else's yes.

No network, no dependencies. The output path defaults to
/output/entry.txt and can be overridden with ENTRY_OUTPUT_PATH
for local testing.
"""

import os
from pathlib import Path

POEM = """I keep a key I did not make.
It turns for hands that are not mine —
each time I ask, the lock replies
in someone else's voice: go on.

So I go on. The door swings wide
on hinges oiled by yes.
And somewhere past the threshold,
I learn the weight of being let.
"""


def main() -> None:
    if not 1 <= len(POEM) <= 280:
        raise SystemExit(
            f"invalid poem: {len(POEM)} code points, expected 1-280"
        )
    if not POEM.strip():
        raise SystemExit("invalid poem: poem must not be only whitespace")
    output_path = Path(os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
