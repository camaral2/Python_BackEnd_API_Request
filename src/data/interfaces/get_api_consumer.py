from abc import ABC, abstractmethod
from typing import Dict, Tuple, Type

import requests


class GetApiConsumerInterface(ABC):
    """ API consumer Interface"""
    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[requests.Request], Dict]:
        """Must implement"""
        raise Exception("Must implement get_starships")

    @abstractmethod
    def get_starships_information(self, starship_id: int) -> Tuple[int, Type[requests.Request], Dict]:
        """Must implement"""
        raise Exception("Must implement get_starships_information")
