from services import (
    get_age,
    get_all_actors,
    Actor
)


# the_oldest_actor = str
# the_youngest_actor = str
# the_oldest_actor_age = int
# the_youngest_actor_age = int
# actor_with_biggest_filmography = str
# actor_who_dead_for_longest_period = str
# the_oldest_movie = str
# actors_with_same_born_year = str
# number_of_dead_actors = str
# average_age_of_actors = int
# average_number_of_movies_per_actor = int

def get_oldeset_actor(actors) -> Actor:
    oldest_actor = actors[0]
    for actor in actors:
        if get_age(actor) > get_age(oldest_actor):
            oldest_actor = actor
    
    return {"oldest_actor": oldest_actor.name, "age": get_age(oldest_actor)}

def get_youngest_actor(actors) -> Actor:
    youngest_actor = actors[0]
    for actor in actors:
        if get_age(actor) < get_age(youngest_actor):
            youngest_actor = actor

    return {"youngest_actor": youngest_actor.name, "age": get_age(youngest_actor)}

# def get_actor_with_biggest_filmography(actors):
#     actor_with_biggest_filmography = actors[0]

print(get_youngest_actor(get_all_actors()))
print(get_oldeset_actor(get_all_actors()))
    