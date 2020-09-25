import datetime
from dataclasses import dataclass


@dataclass
class Athlete:
    name: str
    height: int
    date_of_birth: datetime.date

    @property
    def height_display(self):
        feet, inches = divmod(self.height, 12)
        return f"{feet}'{inches}\""

    @property
    def age(self):
        today = datetime.datetime.now()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
