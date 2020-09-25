# Famous Athletes

[![GitHub Super-Linter](https://github.com/johnnymetz/famous-athletes/workflows/Super-Linter/badge.svg)](https://github.com/marketplace/actions/super-linter)

Generate a random famous athlete for trivia!

## Quickstart

Use the CLI tool. No external python packages are required (only the standard library is used) so the tool is ready to go right out of the box. The only requirement is Python 3.

```
$ python cli.py
LeBron James is 6'9" and 35 years old.

# run again
$ python cli.py
Tiger Woods is 6'1" and 44 years old.

# run with the -s or --search flag to search by name (case-insensitive)
$ python cli.py --search patrick
Patrick Mahomes is 6'3" and 25 years old.

# run with the -q or --quiet flag to print only the name
$ python cli.py --quiet
Rodger Federer

# run with the -v or --verbose flag to print additional metadata (e.g. total athletes, errors
)
$ python cli.py --verbose
Successfully loaded 30 athletes.

Chloe Kim is 5'3" and 20 years old.
```

## Contributors

Add your favorite athlete! See issues for instructions. Linter must pass successfully before code can be merged in.
