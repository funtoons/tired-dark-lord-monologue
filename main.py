#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue (~100 words) to /output/entry.txt.
Deterministic, offline, stdlib only: the text is fixed, no randomness,
no network, no timestamps, no paths in the output.
"""

import os

MONOLOGUE = """Come in. Mind the step \u2014 the third one. It sticks. Always has.

You expected horns. Fire. A speech. I had one once, back when the mountain still smoked and my voice could fill it. These days the mountain is quiet, and so, mostly, am I.

The eclipse gate opens at dusk. My army waits. My generals wait. All that remains is the word. One word, and the valley burns.

Stand there a moment. The candles are warm. The chair opposite is empty, and it has been empty a long time.

You may go. Tell them the Dark Lord is coming. Tell them slowly.
"""

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(MONOLOGUE)

if __name__ == "__main__":
    main()
