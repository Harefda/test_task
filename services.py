from dataclasses import dataclass
import requests, re

from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from typing import Optional
from datetime import (
    datetime,
    date
)
from pydantic import (
    BaseModel,
    validator,
)


class Movie(BaseModel):
    title: str
    year: Optional[str] = None


class Actor(BaseModel):
    name: str
    dob: datetime
    dod: Optional[datetime] = None
    gender: str
    movies: list[Movie]

    @validator("dob", pre=True)
    def parse_dob(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, "%d-%m-%Y")
        return v

    @validator("dod", pre=True)
    def parse_dod(cls, v):
        if isinstance(v, str) and len(re.findall("-", v)) == 2:
            v = re.findall(r'\d{2}-\d{2}-\d{4}', v)[0]
            return datetime.strptime(v, "%d-%m-%Y")
        print("hello", v)

    @validator("name", pre=True)
    def parse_name(cls, v):
        final_name = ""
        full_name = re.findall(r"[A-Z][a-z]+", " "+v)
        for name in full_name:
            final_name += name+" "
        return final_name[0:-1]

    @validator("movies", pre=True)
    def parse_movies(cls, v):
        for movie in v:
            movie["title"] = parse_title(movie["title"])
            movie["year"] = parse_year(movie)
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
    if actor.dod is None:
        return relativedelta(get_current_date(), actor.dob).years
    return relativedelta(actor.dod, actor.dob).years

def parse_title(title):
    count=-1
    parsed_string = ""
    for i in title:
        count+=1
        if i != "/" and title[count-1] != "/":
            parsed_string += i
        else:
            parsed_string += " "

    parsed_string = parsed_string.split()
    return " ".join(parsed_string)

def parse_year(movie):
    if "year" in movie.keys():
        if not isinstance(movie["year"], str):
            movie["year"] = str(movie["year"])
        if isinstance(movie["year"], str):
            year = movie["year"] = re.findall(r"\d+", movie["year"])
            if len(year) == 0:
                movie["year"] = None
            else:
                movie["year"] = year[0]
    else:
        movie["year"] = None
    
    return movie["year"]

print(get_all_actors())