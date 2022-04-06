from services import (
    Actor,
    get_age,
    get_all_actors,
    get_current_date,
    get_period_of_death
)


def get_all_answers(actors):
    oldest_actor = actors[0]
    youngest_actor = actors[0]
    actor_with_biggest_filmography = actors[0]
    actor_dead_for_the_longest_period = actors[0]
    oldest_movie_age = 0
    count_films = 0
    count_dead_actors = 0
    count_alive_actors_age = 0
    current_year = get_current_date().year
    oldest_movie = ""
    actors_with_same_dob = []

    for actor in actors:
        oldest_actor = get_oldeset_actor(actor, oldest_actor)
        youngest_actor = get_youngest_actor(actor, youngest_actor)
        oldest_movie = get_oldest_movie(actor, current_year, oldest_movie, oldest_movie_age)[0]
        oldest_movie_age = get_oldest_movie(actor, current_year, oldest_movie, oldest_movie_age)[1]
        actor_with_biggest_filmography = get_actor_with_biggest_filmography(actor, actor_with_biggest_filmography)
        count_films = get_count_fimls(actor, count_films)
        actor_dead_for_the_longest_period = get_actor_dead_for_the_longest_period(actor, actor_dead_for_the_longest_period)
        count_dead_actors = get_count_dead_actors(actor, count_dead_actors)
        count_alive_actors_age = get_average_age_alive_actors(actor, count_alive_actors_age)
        actors_with_same_dob = get_actors_with_same_dob(actor, actors, actors_with_same_dob)

    return {
        "1": oldest_actor.name,
        "2": youngest_actor.name,
        "3": str(get_age(oldest_actor)),
        "4": str(get_age(youngest_actor)),
        "5": actor_with_biggest_filmography.name,
        "6": actor_dead_for_the_longest_period.name,
        "7": oldest_movie,
        "8": actors_with_same_dob,
        "9": str(count_dead_actors),
        "10": str(count_alive_actors_age // len(actors)),
        "11": str(count_films // len(actors))
    }

def get_oldeset_actor(actor, oldest_actor) -> Actor:
    if get_age(actor) > get_age(oldest_actor):
        oldest_actor = actor
    return oldest_actor

def get_youngest_actor(actor, youngest_actor) -> Actor:
    if get_age(actor) < get_age(youngest_actor):
        youngest_actor = actor
    return youngest_actor

def get_oldest_movie(
    actor,
    current_year,
    oldest_movie,
    oldest_movie_age
):
    for movie in actor.movies:
        if movie["year"] is not None and current_year - int(movie["year"]) > oldest_movie_age:
            oldest_movie = movie["title"]
            oldest_movie_age = get_current_date().year - int(movie["year"])
    return oldest_movie, oldest_movie_age

def get_actor_with_biggest_filmography(actor, actor_with_biggest_filmography):
    if len(actor.movies) > len(actor_with_biggest_filmography.movies):
        return actor
    return actor_with_biggest_filmography

def get_count_fimls(actor, count_fimls):
    count_fimls+=len(actor.movies)
    return count_fimls

def get_actor_dead_for_the_longest_period(actor, actor_dead_for_the_longest_period) -> Actor:
    if actor.dod is not None:
        if get_period_of_death(actor) > get_period_of_death(actor_dead_for_the_longest_period):
            return actor
    return actor_dead_for_the_longest_period

def get_count_dead_actors(actor, count_dead_actors):
    if actor.dod is None:
        count_dead_actors+=1
    return count_dead_actors

def get_average_age_alive_actors(actor, count_alive_actors_age):
    if actor.dod is None:
        count_alive_actors_age+=get_age(actor)
    return count_alive_actors_age

def get_actors_with_same_dob(actor, actors, actors_with_same_dob):
    for nested_actor in actors:
        if actor.dob.year == nested_actor.dob.year and actor.name != nested_actor.name:
            actors_with_same_dob.append(actor.name)
            actors_with_same_dob.append(nested_actor.name)
    return list(set(actors_with_same_dob))

def send_answers(answers):
    pass



print(get_all_answers(get_all_actors()))