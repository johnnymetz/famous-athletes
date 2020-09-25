import argparse
import random

from helpers import get_athletes


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Get a random athlete")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quiet", action="store_true", help="print quiet")
    group.add_argument("-v", "--verbose", action="store_true", help="print verbose")
    return parser


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    athletes = get_athletes("athletes", verbose=args.verbose)
    athlete = random.choice(athletes)
    if args.quiet:
        print(athlete.name)
    else:
        print(
            f"{athlete.name} is {athlete.height_display} and {athlete.age} years old."
        )


if __name__ == "__main__":
    main()
