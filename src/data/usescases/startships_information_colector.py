from typing import Dict, Type
from src.domain.usescases import StarShipsInformationColectorInterface
from src.data.interfaces.get_api_consumer import GetApiConsumerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class StarshipsInformationColector(StarShipsInformationColectorInterface):
    """StarshipsInformationColector usescases"""

    def __init__(self, api_consumer: Type[GetApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def find_starship(self, starship_id: int, time: str) -> Dict:
        api_response = self.__api_consumer.get_starships_information(
            starship_id=starship_id
        )

        if api_response.response["MGLT"] == "unknown":
            raise HttpUnprocessableEntityError("Unprocessible Information for selected starship")

        mglt = api_response.response["MGLT"]
        distance = self.__calculate_distante_travel(mglt, time)

        resp_format = self.__format_api_response(api_response.response, distance)
        
        return resp_format

    @classmethod
    def __calculate_distante_travel(cls, mglt: str, time: str) -> int:
        distante = int(mglt) * int(time)
        return distante

    @classmethod
    def __format_api_response(
        cls, starship_information: Dict, distance_traveled: int
    ) -> Dict:
        """
        Format response from api
        :params - results: List with spaceships informations
        :returns - List with spaceships informations formated
        """
        return {
            "starship": starship_information["name"],
            "model": starship_information["model"],
            "manufacturer": starship_information["manufacturer"],
            "max_atmosphering_speed": starship_information["max_atmosphering_speed"],
            "MGLT": starship_information["MGLT"],
            "distance_traveled": str(distance_traveled) + " ML/h",
        }


# "id": starship_information["url"].split("/")[-2],
# "hyperdrive_rating": starship_information["hyperdrive_rating"],
