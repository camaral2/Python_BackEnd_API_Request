from collections import namedtuple
from typing import Type, Tuple, Dict
from faker import Faker

import requests

fake = Faker()


def mock_starships():
    """mock data for starships
    :return - dict with starships information
    """

    return {
        "name": fake.name(),
        "model": fake.name(),
        "manufacturer": fake.name(),
        "cost_in_credits": fake.random_int(),
        "length": fake.random_int(),
        "max_atmosphering_speed": fake.random_int(),
        "hyperdrive_rating": fake.random_int(),
        "MGLT": fake.random_int(),
        "url": "https://swapi.dev/api/starships/{}/".format(fake.random_int()),
    }


class GetApiConsumerSpy:
    """Spy for GetApiConsumer"""

    def __init__(self) -> None:
        self.get_starships_resp = namedtuple(
            "GET_Starships", "status_code request response"
        )
        self.get_starships_attributes = {}

        self.get_starships_information_resp = namedtuple(
            "GET_Starships_Information", "status_code request response"
        )
        self.get_starships_information_attributes = {}

    def get_starships(self, page: int) -> Tuple[int, Type[requests.Request], Dict]:
        """Mock to get_starships"""
        self.get_starships_attributes["page"] = page
        return self.get_starships_resp(
            status_code=200,
            request=None,
            response={
                "results": [
                    mock_starships(),
                    mock_starships(),
                    mock_starships(),
                    mock_starships(),
                ]
            },
        )

    def get_starships_information(
        self, starship_id: int
    ) -> Tuple[int, Type[requests.Request], Dict]:
        """Mock to get_starships_information"""
        self.get_starships_information_attributes["starship_id"] = starship_id
        return self.get_starships_information_resp(
            status_code=200, request=None, response=mock_starships()
        )
