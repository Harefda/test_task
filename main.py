from services import (
    convert_str_to_date,
    get_age,
    get_all_actors,
    Actor,
    get_current_date
)
import os


def get_oldeset_actor(actors):
    oldest_actor = actors[0]
    for actor in actors:
        if get_age(actor) > get_age(oldest_actor):
            oldest_actor = actor
    
    return {"oldest_actor": oldest_actor.name, "age": get_age(oldest_actor)}

def get_youngest_actor(actors):
    youngest_actor = actors[0]
    for actor in actors:
        if get_age(actor) < get_age(youngest_actor):
            youngest_actor = actor

    return {"youngest_actor": youngest_actor.name, "age": get_age(youngest_actor)}

def get_oldest_movie(actors):
    current_year = get_current_date().year
    oldest_movie = ""
    oldest_movie_age = 0
    for actor in actors:
        for movie in actor.movies:
            if movie["year"] is not None and current_year - int(movie["year"]) > oldest_movie_age:
                oldest_movie = movie["title"]
                oldest_movie_age = get_current_date().year - int(movie["year"])

    return oldest_movie

# def get_actor_with_biggest_filmography(actors):
#     actor_with_biggest_filmography = actors[0]

# print(get_youngest_actor(get_all_actors()))
# print(get_oldeset_actor(get_all_actors()))
# print(get_oldest_movie(get_all_actors()))

print(os.getenv("AUTH_PASSWORD"))