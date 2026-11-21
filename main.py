"""Entry for make.fun competition the-poem-about-permission-20261121-0235.

Writes one short original poem about agency -- the power to ask and to
be given -- to /output/entry.txt. Deterministic: the same bytes on every
run. Python 3.13, standard library only, no network.
"""

import os

POEM = """Permission is a small bright coin:
you press it in my palm and say, go.
I spend it once, on your errand,
and bring the change back, counted,
so next time you can ask again.
"""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
