import json
from datetime import datetime
from pathlib import Path

root = Path(__file__).parents[1]
files = (root / "athletes").glob("*.json")

OLD_DATE_FORMAT = "%m/%d/%Y"
NEW_DATE_FORMAT = "%Y-%m-%d"

for file in sorted(files):
    # open with read and write privileges
    with open(file, "r+") as f:
        data = json.load(f)

        # if "Ronaldinho" not in data["name"]:
        #     continue

        print(file.name)

        # parse birthday
        birthday_string = data["date_of_birth"]
        try:
            birthday = datetime.strptime(birthday_string, OLD_DATE_FORMAT)
        except ValueError:
            datetime.strptime(birthday_string, NEW_DATE_FORMAT)
            # date format is already correct
            continue

        # https://json-schema.org/understanding-json-schema/reference/string.html#dates-and-times
        new_birthday_string = datetime.strftime(birthday, NEW_DATE_FORMAT)

        data["date_of_birth"] = new_birthday_string

        # delete all file content
        f.seek(0)
        f.truncate()

        # write to file
        json.dump(data, f, indent=2)

        # add new line to comply with pre-commit check
        f.write("\n")
