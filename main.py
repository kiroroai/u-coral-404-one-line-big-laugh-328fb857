#!/usr/bin/env python3
"""One Line, Big Laugh — writes a single original funny line to /output/entry.txt.

Python 3, standard library only, deterministic, no network.
"""

import os

LINE = "I asked my air fryer for life advice. It said 'shake halfway through' \u2014 and honestly, it's the wisest thing I've heard in years."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
