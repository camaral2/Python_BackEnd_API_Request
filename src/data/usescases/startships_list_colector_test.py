# from src.util.test.get_api_consumer import GetApiConsumerSpy
from src.util.test.get_api_consumer import GetApiConsumerSpy
from .startships_list_colector import StarshipsListColector


def test_list():
    """test with Spy"""
    api_consumer = GetApiConsumerSpy()
    startships_list_colector = StarshipsListColector(api_consumer=api_consumer)

    page = 1
    response = startships_list_colector.list(page=page)

    assert api_consumer.get_starships_attributes == {"page": page}
    assert isinstance(response, list)
    assert "id" in response[0]
    assert "MGLT" in response[0]
