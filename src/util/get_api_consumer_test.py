from src.errors.http_request_error import HttpRequestError
from .get_api_consumer import GetApiConsumer


def test_get_starships(requests_mock):
    """Testing get_starships method"""

    requests_mock.get(
        "https://swapi.dev/api/starships/",
        status_code=200,
        json={"some": "thing", "results": [{}]},
    )

    api_consumer = GetApiConsumer()
    ret = api_consumer.get_starships(page=1)

    assert ret.request.method == "GET"
    assert ret.status_code == 200
    assert isinstance(ret.response["results"], list)


def test_get_starships_http_error(requests_mock):
    """Test error in test_get_starships_http_error"""

    requests_mock.get(
        "https://swapi.dev/api/starships/",
        status_code=404,
        json={"detail": "something"},
    )
    api_consumer = GetApiConsumer()

    try:
        api_consumer.get_starships(page=100)

        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None
