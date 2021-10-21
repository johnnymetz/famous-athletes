"""
Need to pip install jsonschema to run this.
"""

import json

from jsonschema import FormatChecker, validate

# with open("schema.json") as f:
#     schema = json.load(f)


# with open("athletes/devin_booker.json") as f:
#     data = json.load(f)


schema = {
    "title": "Athlete",
    "type": "object",
    "properties": {"birthday": {"type": "string", "format": "date"}},
}

# data = {"birthday": "xxx"}
data = {"birthday": "2020-10-20"}


validate(data, schema, format_checker=FormatChecker())
