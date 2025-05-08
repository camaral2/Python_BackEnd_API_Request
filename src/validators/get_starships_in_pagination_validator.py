from cerberus import Validator
from src.errors import HttpUnprocessableEntityError


def get_pagination_validator(request: any):
    """AI is creating summary for get_pagination_validator

    Args:
        request (any): [description]
    """
    query_param_validator = Validator({"page": {"type": "string", "required": True}})

    response = query_param_validator.validate(request.query_params)
    print(response)

    if response is False:
        raise HttpUnprocessableEntityError(query_param_validator.errors)
