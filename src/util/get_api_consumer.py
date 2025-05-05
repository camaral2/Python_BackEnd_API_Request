from collections import namedtuple
from typing import Type, Tuple, Dict
import requests
from src.errors import HttpRequestError


class GetApiConsumer:
    """Get info API"""

    def __init__(self) -> None:
        self.get_starships_resp = namedtuple(
            "GET_Starships", "status_code request response"
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
