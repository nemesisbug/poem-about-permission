"""Write the poem about permission to /output/entry.txt.

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
    output_path = Path(os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
