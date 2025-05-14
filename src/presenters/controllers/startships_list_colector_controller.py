from typing import Type, Dict
from src.domain.usescases.starships_list_colector import StarShipsListColectorInterface


class StarshipsListColetorController:
    """ Controler to List Starships """
    def __init__(
        self, starships_list_colector: Type[StarShipsListColectorInterface]
    ) -> None:
        self.__user_case = starships_list_colector

    def handle(self, http_request: Dict):
        """ Handler to list colector """
        page = http_request["query_params"]["page"]
        starship_list = self.__user_case.list(page)

        http_response = {"status_code": 200, "data": starship_list}

        return http_response
