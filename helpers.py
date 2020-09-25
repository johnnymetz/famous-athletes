import datetime
import json
import random
from pathlib import Path
from typing import List

from models import Athlete


def get_athletes(directory: str, verbose: bool = False) -> List[Athlete]:
    athletes = []
    for file_name in Path(directory).glob("*.json"):
        with open(file_name) as f:
            try:
                data = json.load(f)
                athletes.append(
                    Athlete(
                        name=data["name"],
                        height=data["height"],
                        date_of_birth=datetime.datetime.strptime(
                            data["date_of_birth"], "%m/%d/%Y"
                        ),
                    )
                )
            except Exception as e:
                if verbose:
                    print(f"Unable to parse {file_name}: {e}")

    if verbose:
        print(f"Successfully loaded {len(athletes)} athletes.\n")

    return athletes


def search_by_name(name: str, athletes: List[Athlete]) -> List[Athlete]:
    found = []
    for athlete in athletes:
        if name.lower() in athlete.name.lower():
            found.append(athlete)
    return found


def get_random_athlete(search: str, quiet: str, verbose: bool):
    athletes = get_athletes("athletes", verbose=verbose)
    if search:
        athletes = search_by_name(search, athletes)
    if not athletes:
        return

    athlete = random.choice(athletes)

    if quiet:
        return athlete.name
    else:
        return (
            f"{athlete.name} is {athlete.height_display} and {athlete.age} years old."
        )
