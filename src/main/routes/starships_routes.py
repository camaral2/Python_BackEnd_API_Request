from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.validators.get_starships_in_pagination_validator import get_pagination_validator
from src.validators.get_starships_information_validator import get_information_validator
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.get_starships_in_pagination_composers import get_starships_in_pagination_composers
from src.main.composers.get_starships_information_composers import get_starships_information_composers
from src.presenters.errors.error_controller import handle_errors

startships_routes = APIRouter()


@startships_routes.get("/api/starships/list")
async def get_starships_in_pagination(request: RequestFastApi):
    """AI is creating summary for get_starships_in_pagination

    Args:
        request (RequestFastApi): [description]

    Returns:
        [type]: [description]
    """
    response = None
    controller = get_starships_in_pagination_composers()

    try:
        get_pagination_validator(request)
        response = await request_adapter(request, controller.handle)
    except Exception as e:
        response = handle_errors(e)

    return JSONResponse(
        status_code=response["status_code"], content={"data": response["data"]}
    )


@startships_routes.get("/api/starships/information")
async def get_starships_information(request: RequestFastApi):
    ''' get_starships_information '''

    response = None
    controller = get_starships_information_composers()

    try:
        await get_information_validator(request)
        response = await request_adapter(request, controller.handle)
    except Exception as e:
        response = handle_errors(e)
        
    return JSONResponse(
        status_code=response["status_code"], content={"data": response["data"]}
    )
