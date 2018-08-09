import os
import jinja2
import aiohttp_jinja2
from aiohttp import web
from app import homepage, badge_view, report_view, discover_github_repo


BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

def setup_routes(app):
    app.router.add_get('/', homepage)
    app.router.add_get('/badge', badge_view)
    app.router.add_get('/report', report_view)
    app.router.add_get('/discover', discover_github_repo)


def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    setup_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    web.run_app(app)

async def run():
    return create_app()