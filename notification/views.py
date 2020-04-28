from aiohttp import web
from aiohttp_validate import validate

from notification import validators
from notification.fcm import send_push_new_message


async def index_greet(request):
    return web.Response(text='Hello!')


@validate(
    request_schema=validators.notification_request_scheme,
    response_schema=validators.notification_response_scheme,
)
async def notification(payload, request):
    async with request.app['db'].acquire() as conn:
        await send_push_new_message(conn, **payload)
    return web.json_response({'message': 'good', 'code': 200, **payload})
