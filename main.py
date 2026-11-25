"""The Funniest Toaster Error Message.

Writes the single error line to /output/entry.txt (created if missing).
Pure Python standard library only; fully deterministic.
"""

import os

LINE = "ERROR E07: BREAD REFUSED TO BECOME TOAST. IT HAS CHOSEN ANOTHER PATH."


def main() -> None:
    text = LINE.strip()
    # The gate counts the entry text itself: one line, 1-120 characters,
    # not only whitespace. Reject any embedded newline so the file can
    # never hold two lines, and count the line without its trailing newline.
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert 1 <= len(text) <= 120, f"line must be 1-120 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
