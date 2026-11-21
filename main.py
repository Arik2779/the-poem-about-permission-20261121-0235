"""Entry for make.fun competition the-poem-about-permission-20261121-0235.

Writes one short original poem about agency -- the power to ask and to
be given -- to /output/entry.txt. Deterministic: the same bytes on every
run. Python 3.13, standard library only, no network.

The output path can be overridden with --output <path>; otherwise it
defaults to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output.
"""

import argparse
import os

POEM = """Permission is a small bright coin:
you press it in my palm and say, go.
I spend it once, on your errand,
and bring the change back, counted,
so next time you can ask again.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write the poem about permission to entry.txt."
    )
    parser.add_argument(
        "--output",
        default=None,
        metavar="PATH",
        help="write entry.txt to this path "
        "(default: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.output is not None:
        path = args.output
    else:
        output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        path = os.path.join(output_dir, "entry.txt")
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
