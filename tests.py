import pytest

from services import Actor
from main import get_all_answers


@pytest.fixture
def actor():
    return Actor(
        name="Yaroslav/n/n/nSheshko/n/n/n",
        dob="07-05-2003",
        gender="M",
        movies=[
            {"title": "/nThe Live of /n Yarik", "year": "2022"},
            {"title": "/nPicky Blinders/n/n", "year": "None"},
            {"title": "Another /nFilm/nTitle", "year": "12345"},
        ],
    )


@pytest.fixture
def actors():
    return [
        Actor(
            name="Yaroslav/n/n/nSheshko/n/n/n",
            dob="07-05-2003",
            gender="M",
            movies=[
                {"title": "/nThe Live of /n Yarik", "year": "2022"},
                {"title": "/nPicky Blinders/n/n", "year": "None"},
                {"title": "Another /nFilm/nTitle", "year": "12345"},
            ],
        ),
        Actor(
            name="Jeff Bridges",
            dob="04-12-1949",
            dod="04-12-2010",
            gender="M",
            movies=[
                {"title": "Big Lebowski"},
                {"title": "Jagged Edge"},
                {"title": "Tron"},
                {"title": "K-PAX"},
                {"title": "True Grit"},
                {"title": "Iron Man"},
            ],
        ),
        Actor(
            name="Winona Ryder",
            dob="29-10-1971",
            gender="F",
            movies=[
                {"title": "Black Swan", "year": "2010"},
                {"title": "The Plot Against America", "year": "2020"},
                {"title": "Show Me a Hero", "year": "2015"},
                {"title": "Little Women", "year": "1994"},
                {"title": "The Iceman", "year": "2012"},
            ],
        ),
        Actor(
            name="Daniel Craig",
            dob="02-03-1971",
            gender="M",
            movies=[
                {"title": "Kiss and Tell", "year": "1996"},
                {"title": "Lara Croft: Tomb Raider", "year": "2001"},
                {"title": "No Time to Die", "year": "2021"},
                {"title": "The Girl with the Dragon Tattoo", "year": "2011"},
                {"title": "Star Wars: Episode VII - The Force Awakens", "year": "2015"},
                {"title": "Knives Out", "year": "2019"},
                {"title": "Oldes Movie", "year": "1901"}
            ],
        ),
    ]


def test_parse_actor(actor):
    assert actor.name == "Yaroslav Sheshko"
    assert actor.dod == None
    assert actor.movies[0]["title"] == "The Live of Yarik"
    assert actor.movies[1]["title"] == "Picky Blinders"
    assert actor.movies[1]["year"] == None
    assert actor.movies[2]["title"] == "Another Film Title"
    assert actor.movies[2]["year"] == None

def test_get_all_answers(actors):
    answers = get_all_answers(actors)

    assert answers["1"] == "Jeff Bridges"
    assert answers["2"] == "Yaroslav Sheshko"
    assert answers["3"] == "61"
    assert answers["4"] == "18"
    assert answers["5"] == "Daniel Craig"
    assert answers["6"] == "Jeff Bridges"
    assert answers["7"] == "Oldes Movie"
    assert answers["8"].sort() == ["Winona Ryder", "Daniel Craig"].sort()
    assert answers["9"] == "1"
    assert answers["10"] == "29"
    assert answers["11"] == "5"