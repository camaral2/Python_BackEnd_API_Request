from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.validators.get_starships_in_pagination_validator import (
    get_pagination_validator,
)

from src.main.adapters.request_adapter import request_adapter
from src.main.composers.get_starships_in_pagination_composers import (
    get_starships_in_pagination_composer,
)

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
        controller = get_starships_in_pagination_composer()

        resposta = await request_adapter(request, controller.handle)

        return JSONResponse(
            status_code=resposta["status_code"], content={"data": resposta["data"]}
        )

    except Exception as e:
        return JSONResponse(status_code=422, content=e.message)
