from src.data.usescases.startships_information_colector import (
    StarshipsInformationColector,
)
from src.util.test.get_api_consumer import GetApiConsumerSpy

def test_find_starship():
    """Testing find starship method"""
    api_consumer = GetApiConsumerSpy()
    startships_information_colector = StarshipsInformationColector(api_consumer)

    starship_id = 9
    time = 4

    response = startships_information_colector.find_starship(
        starship_id=starship_id, time=time
    )

    assert (
        api_consumer.get_starships_information_attributes["starship_id"] == starship_id
    )
    assert isinstance(response, dict)
    assert "MGLT" in response
    assert "distance_traveled" in response
