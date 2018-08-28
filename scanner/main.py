import os
import logging
import aiohttp_jinja2
import jinja2
from aiohttp import web

from app import badge_view, homepage, report_view, report_view_json, error_middleware
from background_worker import start_background_tasks, cleanup_background_tasks


BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

logging.basicConfig(format='%(asctime)s %(message)s')
log = logging.getLogger()
log.setLevel(logging.INFO)


def setup_routes(app):
    app.router.add_get('/', homepage)
    app.router.add_get('/badge/{source}/{owner}/{repo}', badge_view)
    app.router.add_get('/report/{source}/{owner}/{repo}/json', report_view_json)
    app.router.add_get('/report/{source}/{owner}/{repo}', report_view)


def create_app():
    app = web.Application(middlewares=[error_middleware, ])
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    setup_routes(app)
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)
    return app


if __name__ == '__main__':
    app = create_app()
    web.run_app(app)


async def run():
    return create_app()
