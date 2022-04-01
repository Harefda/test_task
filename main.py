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


def get_oldeset_actor(all_actors) -> Actor:
    the_oldest_actor = all_actors[0]
    for actor in all_actors:
        if get_age(actor) > get_age(the_oldest_actor):
            the_oldest_actor = actor
    
    return the_oldest_actor

def get_youngest_actor(all_actors) -> Actor:
    the_youngest_actor = all_actors[0]
    for actor in all_actors:
        if get_age(actor) < get_age(the_youngest_actor):
            the_youngest_actor = actor

    return the_youngest_actor

print(get_oldeset_actor(get_all_actors()).name, get_age(get_oldeset_actor(get_all_actors())))