#!/usr/bin/env python3
"""Vending Machine Pickup Line entry: writes one flirty pickup line to /output/entry.txt."""

import os

LINE = "Are you a snack? Because I've been holding a cold drink and warm feelings for you all day — insert coin to continue."

# Self-check: the entry must stay one line of at most 200 characters, with no
# leading or trailing whitespace padding the pickup line.
assert "\n" not in LINE and 1 <= len(LINE) <= 200
assert LINE == LINE.strip()

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Self-check: the file on disk must hold exactly the validated line.
    assert open("/output/entry.txt", encoding="utf-8").read() == LINE

if __name__ == "__main__":
    main()
