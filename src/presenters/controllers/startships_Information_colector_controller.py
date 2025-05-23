from typing import Type, Dict
from src.domain.usescases.starships_information_colector import StarShipsInformationColectorInterface

class StarshipsInformationColetorController:
    """Controler to Information Starships"""

    def __init__(
        self,
        starships_information_colector: Type[StarShipsInformationColectorInterface],
    ) -> None:
        self.__user_case = starships_information_colector

    def handle(self, http_request: Dict):
        """Handler to list colector"""

        starship_id = http_request["body"]["starship_id"]
        time = http_request["body"]["time"]

        starship_info = self.__user_case.find_starship(
            starship_id=starship_id, time=time
        )

        http_response = {"status_code": 200, "data": starship_info}

        return http_response
