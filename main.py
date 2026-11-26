#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun entry.

Writes one funny text message from the writer's future self to
/output/entry.txt (and prints it). The message is under 200 characters,
needs no setup, and lands its joke by the last line.
"""

import os

MESSAGE = (
    "Future you here. You changed your password AGAIN. "
    "The recovery email is an account you deleted in 2024. "
    "I'm locked out of everything. Write it down. On paper. Like an animal."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(MESSAGE) <= 200, f"message is {len(MESSAGE)} chars, must be 1-200"
    assert MESSAGE.strip(), "message must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(MESSAGE)
    print(MESSAGE)


if __name__ == "__main__":
    main()
