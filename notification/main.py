import logging
import os.path
import sys

from aiohttp import web

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from notification.db import close_pg, init_pg
from notification.settings import config
from notification.middleware import setup_middlewares
from notification.routes import setup_routes


async def web_app():
    app = web.Application()
    app['config'] = config
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    setup_middlewares(app)
    setup_routes(app)
    return app

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    disabled_loggers = ['urllib3.connectionpool', 'urllib3.util.retry']
    for logger_name in disabled_loggers:
        logger = logging.getLogger(logger_name)
        logger.disabled = True
    app = web_app()
    web.run_app(app)
