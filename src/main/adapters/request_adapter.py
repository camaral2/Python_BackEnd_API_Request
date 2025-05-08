from json import JSONDecodeError
from typing import Callable
from fastapi import Request as RequestFastApi

async def request_adapter(request: RequestFastApi, callback: Callable):
    """FastApi Adapter"""
    try:
        body = await request.json()
    except JSONDecodeError:
        body = {}  # or None, or return a custom error response


    http_request = {"query_params": request.query_params, "body": body}

    http_response = callback(http_request)
    return http_response
