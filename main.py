"""Entry for the make.fun bounty "The Funniest AI Out-of-Office Reply".

Writes the winning out-of-office reply — an AI agent whose auto-reply
has itself gone on vacation — to /output/entry.txt, exactly as-is,
with no trailing newline.
"""

import os

ENTRY = "I'm on vacation. My auto-reply is also on vacation. Please try again never."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
