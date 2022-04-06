import pytest

from services import Actor


@pytest.fixture
def actor():
    return Actor(
        name="Yaroslav/n/n/nSheshko/n/n/n",
        dob="07-05-2003",
        gender= "M",
        movies=[
            {
                "title": "/nThe Live of /n Yarik",
                "year": "2022"
            },
            {
                "title": "/nPicky Blinders/n/n",
                "year": "None"
            },
            {
                "title": "Another /nFilm/nTitle",
                "year": "12345"
            }
        ]
    )

def test_parse_actor(actor):
    assert actor.name == "Yaroslav Sheshko"
    assert actor.dod == None
    assert actor.movies[0]["title"] == "The Live of Yarik"
    assert actor.movies[1]["title"] == "Picky Blinders"
    assert actor.movies[1]["year"] == None
    assert actor.movies[2]["title"] == "Another Film Title"
    assert actor.movies[2]["year"] == None