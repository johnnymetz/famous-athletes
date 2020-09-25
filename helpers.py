import datetime
import json
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
