class HttpRequestError(Exception):
    """AI is creating summary for http_request_error

    Args:
        Exception ([type]): [description]
    """

    def __init__(self, message: str, status_code: int) -> None:
        """AI is creating summary for __init__

        Args:
            message (str): [description]
            status_code (int): [description]
        """
        super().__init__(message)
        self.message = message
        self.status_code = status_code