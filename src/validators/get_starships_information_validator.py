from cerberus import Validator
from src.errors import HttpUnprocessableEntityError

async def get_information_validator(request: any):
    """AI is creating summary for get_information_validator

    Args:
        request (any): [description]

    Raises:
        HttpUnprocessableEntityError: [description]
    """

    body = None

    try:
        body = await request.json()
    except:
        pass

    body_param_validator = Validator(
        {"starship_id": {"type": "integer", "required": True},
        "time": {"type": "integer", "required": True}},
    )

    response = body_param_validator.validate(body)

    if response is False:
        raise HttpUnprocessableEntityError(body_param_validator.errors)
