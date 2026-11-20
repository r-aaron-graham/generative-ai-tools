"""Render a reusable prompt with strict, explicit input fields."""
import argparse
from string import Template

PROMPT = Template("Summarize the following material for $audience.\n"
                  "Use only the supplied material and identify missing information.\n\n"
                  "<material>\n$material\n</material>\n")


def render(audience, material):
    if not audience.strip() or not material.strip():
        raise ValueError("Audience and material must both be nonempty")
    if len(audience) > 200 or len(material) > 20000:
        raise ValueError("Audience or material exceeds the supported length")
    return PROMPT.substitute(audience=audience, material=material)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audience", required=True)
    parser.add_argument("--material", required=True)
    args = parser.parse_args()
    try:
        print(render(args.audience, args.material))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
