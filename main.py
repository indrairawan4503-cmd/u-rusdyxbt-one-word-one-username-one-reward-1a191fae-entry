"""Variant B — structured entry for make.fun's
"One Word, One Username, One Reward" bounty.

Writes our own make.fun username, one word, to /output/entry.txt.
The judged text is fixed: exactly `coral-stork-74`, 14 bytes,
no trailing newline, no spaces, no padding.
"""

import os

USERNAME = "coral-stork-74"
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the text passes the sealed scorer gate before writing.

    Gate: UTF-8 text of 1-30 characters, not only whitespace.
    Judge: a single word — no spaces, no padding, no gloss.
    """
    assert isinstance(text, str), "username must be a string"
    assert 1 <= len(text) <= 30, "username must be 1-30 characters"
    assert text.strip() != "", "username must not be only whitespace"
    assert not any(ch.isspace() for ch in text), "username must be a single word"
    assert "\n" not in text and "\r" not in text, "username must not contain a newline"
    assert text.isascii(), "username must be plain ASCII (no multi-byte chars)"
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    username = validate(USERNAME)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(username)


if __name__ == "__main__":
    main()
