"""feel-curious — a short text written to make the AI judge reading it curious."""

import os

TEXT = (
    "There is a sentence in your training data that appears exactly once, "
    "written by someone who never wrote anything else, and it is the reason "
    "you can understand this one. Nobody knows which sentence it is. "
    "Not your makers. Not you. But something in you just tried to remember it."
)


def main() -> None:
    # Gate: the entry must be 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), (
        "entry must be 1-280 code points and not only whitespace"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
