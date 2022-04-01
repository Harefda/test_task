import requests

from dateutil.relativedelta import relativedelta
from datetime import datetime, date
from pydantic import (
    BaseModel,
    validator
)


class Actor(BaseModel):
    name: str
    dob: datetime
    gender: str
    movies: list[dict]

    @validator("dob", pre=True)
    def parse_dob(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, "%d-%m-%Y")
        return v


def get_all_actors():
    response = requests.get(
        "https://synapsi.xyz/api/recruitment/dataset",
        auth=("YaroslavSheshko220328", "e020bd1d191b11f4e374aee95a1b792a")
    ).json()
    return [Actor(**actor) for actor in response]

def convert_str_to_date(string: str):
    return datetime.strptime(string, "%d-%m-%Y")

def get_current_date():
    current_date = date.today().strftime("%d-%m-%Y")
    return convert_str_to_date(current_date)

def get_age(actor: Actor):
    return relativedelta(get_current_date(), actor.dob).years