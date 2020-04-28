import re

from aiohttp import web

from notification import settings


def is_exclude(request, exclude):
    for pattern in exclude:
        if re.fullmatch(pattern, request.path):
            return True
    return False


def setup_middlewares(app):
    middlewares = [
        token_auth_middleware(exclude_routes=('/great/', )),
    ]
    app.middlewares.extend(middlewares)


def token_auth_middleware(
    request_property='user',
    auth_scheme='Token',
    exclude_routes=(),
    exclude_methods=(),
):

    @web.middleware  # noqa WPS430
    async def middleware(request, handler):  # noqa WPS110
        if is_exclude(request, exclude_routes) or request.method in exclude_methods:
            return await handler(request)

        try:
            scheme, token = request.headers['Authorization'].strip().split(' ')
        except KeyError:
            raise web.HTTPUnauthorized(reason='Missing authorization header')
        except ValueError:
            raise web.HTTPForbidden(reason='Invalid authorization header')
        if auth_scheme.lower() != scheme.lower():
            raise web.HTTPForbidden(reason='Invalid token scheme')

        if settings.TOKEN != token:
            raise web.HTTPForbidden(reason='Token doesnt exist')

        return await handler(request)

    return middleware
