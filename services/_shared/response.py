from http.client import INTERNAL_SERVER_ERROR, OK
from typing import Any

from rest_framework import response


def _make_response(data: Any, status: int):
    return response.Response(data=data, status=status)


def make_error_response(message: str = None, status=INTERNAL_SERVER_ERROR):
    return _make_response(
        data={'message': message or 'Something went wrong'},
        status=status
    )


def make_success_response(data: Any=None, status=OK):
    content = {'data': data}

    is_paginated_response = type(data) is dict and data.get('data') and data.get('meta') and data['meta'].get('pagination_links')
    if is_paginated_response:
        content = data

    return _make_response(data=content, status=status)
