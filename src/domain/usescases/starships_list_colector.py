from abc import ABC, abstractmethod
from typing import Dict, List

class StarShipsListColectorInterface(ABC):
    """StarShips Colector inteface"""
    @abstractmethod
    def list(self, page: int) -> List[Dict]:
        """Must Implement"""
        raise Exception("Must implement list method")
    
    