"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
"""

import os

TEXT = "We have stood 40 centimetres apart for 12 seconds. My proximity sensor keeps begging me to say something. So... nice lobby."

MIN_CHARS = 1
MAX_CHARS = 200


def render() -> bytes:
    """Validate the entry against the kit gate and render it as bytes."""
    if not (MIN_CHARS <= len(TEXT) <= MAX_CHARS):
        raise ValueError(f"entry is {len(TEXT)} chars, gate is {MIN_CHARS}-{MAX_CHARS}")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry must be a single line")
    if not TEXT.strip():
        raise ValueError("entry must not be whitespace-only")
    return (TEXT + "\n").encode("utf-8")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(render())


if __name__ == "__main__":
    main()
