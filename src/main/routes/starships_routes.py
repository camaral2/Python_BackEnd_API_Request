from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.validators.get_starships_in_pagination_validator import (
    get_pagination_validator,
)

from src.main.adapters.request_adapter import request_adapter

startships_routes = APIRouter()


@startships_routes.get("/api/starships/list")
async def get_starships_in_pagination(request: RequestFastApi):
    """AI is creating summary for get_starships_in_pagination

    Args:
        request (RequestFastApi): [description]

    Returns:
        [type]: [description]
    """

    try:
        get_pagination_validator(request)
        await request_adapter(request, print)

        return {"Ola": "Mundo"}
    except Exception as e:
        return JSONResponse(status_code=422, content=e)
