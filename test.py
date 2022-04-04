from services import Actor
import re

actor_info = {
"name": "Robin Williams/n/m",
"dob": "21-07-1951",
"gender": "M",
"movies": [
{
"title": "Dead Again",
"year": "11111"
},
{
"title": "Good Morning, Vietnam",
"year": "1987"
},
{
"title": "Mrs. Doubtfire",
"year": "1993"
},
{
"title": "Flubber",
"year": "1997"
},
{
"title": "Jumanji",
"year": "1995"
},
{
"title": "Patch Adams",
"year": "1998"
},
{
"title": "Dead Poets Society",
"year": "argarhaerh/n1989"
},
{
"title": "Good Will Hunting",
"year": "/t2008"
},
{
"title": "Jakob The Liar",
"year": 1999
},
{
"title": "Patch Adams",
"year": "None"
},
{
"title": "Good Will Hunting"
},
{
"title": "Mrs. Doubtfire",
"year": "2022adskjfasdfasdf"
}
]
}

actor = Actor(**actor_info)

def parse_movies(actor):
    for movie in actor.movies:
        if not isinstance(movie.year, str):
            movie.year = str(movie.year)
        if isinstance(movie.year, str):
            year = movie.year = re.findall(r"\d+",movie.year)
            if len(year) == 0:
                movie.year = None
            else:
                movie.year = year[0]
        if movie.year is not None and len(movie.year) !=4:
            movie.year = None

    return actor.movies

def delete_stuff(string):
    count=-1
    parsed_string = ""
    for i in string:
        count+=1
        if i != "/" and string[count-1] != "/":
            parsed_string += i
        else:
            parsed_string += " "

    parsed_string = parsed_string.split()
    return " ".join(parsed_string)