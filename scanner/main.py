from aiohttp import web

from app import scan

def setup_routes(app):
    app.router.add_get('/', scan)

app = web.Application()
setup_routes(app)
web.run_app(app)