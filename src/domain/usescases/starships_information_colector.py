from abc import ABC, abstractmethod
from typing import Dict, List

class StarShipsInformationColectorInterface(ABC):
    """StarShips Information Colector inteface"""
    @abstractmethod
    def find_starship(self, starship_id: int, time: str) -> Dict:
        """Must Implement"""
        raise Exception("Must implement find_starship method")
    
    