import argparse

from helpers import get_random_athlete


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Get a random athlete")
    parser.add_argument('-s', "--search", help="Search by name")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quiet", action="store_true", help="print quiet")
    group.add_argument("-v", "--verbose", action="store_true", help="print verbose")
    return parser


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    random_athlete = get_random_athlete(
        search=args.search, quiet=args.quiet, verbose=args.verbose
    )
    print(random_athlete if random_athlete else "No athletes found")


if __name__ == "__main__":
    main()
