from collections import namedtuple
from typing import Type, Tuple, Dict
import requests
from src.errors import HttpRequestError
from src.data.interfaces.get_api_consumer import GetApiConsumerInterface


class GetApiConsumer(GetApiConsumerInterface):
    """Get info API"""

    def __init__(self) -> None:
        self.get_starships_resp = namedtuple(
            "GET_Starships", "status_code request response"
        )

        self.get_starships_information_resp = namedtuple(
            "GET_Starships_Information", "status_code request response"
        )

    def get_starships(self, page: int) -> Tuple[int, Type[requests.Request], Dict]:
        """request starships in paginnation

        Args:
            page (int): With page of navegation

        Raises:
            HttpRequestError: [description]

        Returns:
            Tuple[int, Type[requests.Request], Dict]: status_code, request, respose attributes
        """
        params = {"page": page}

        req = requests.Request(
            method="GET", url="https://swapi.dev/api/starships/", params=params
        )

        req_prepared = req.prepare()
        resp = self.__send_http_request(req_prepared)
        status_code = resp.status_code

        if status_code == 200:
            return self.get_starships_resp(
                status_code=status_code, request=req, response=resp.json()
            )
        else:
            raise HttpRequestError(
                message=resp.json()["detail"], status_code=status_code
            )

    def get_starships_information(
        self, starship_id: int
    ) -> Tuple[int, Type[requests.Request], Dict]:
        """request starships in information

        Args:
            starship_id (int): Id for information of starship

        Raises:
            HttpRequestError: [description]

        Returns:
            Tuple[int, Type[requests.Request], Dict]: status_code, request, respose attributes
        """

        req = requests.Request(
            method="GET",
            url=f"https://swapi.dev/api/starships/{starship_id}",
        )

        req_prepared = req.prepare()
        resp = self.__send_http_request(req_prepared)
        status_code = resp.status_code

        if status_code == 200:
            return self.get_starships_information_resp(
                status_code=status_code, request=req, response=resp.json()
            )
        else:
            raise HttpRequestError(
                message=resp.json()["detail"], status_code=status_code
            )

    @classmethod
    def __send_http_request(cls, req_prepared: Type[requests.Request]) -> any:
        """AI is creating summary for __send_http_request

        Args:
            req_prepared (Type[requests.Request]): [description]

        Returns:
            any: [description]
        """
        http_session = requests.Session()
        resp = http_session.send(req_prepared, verify=False)
        return resp
