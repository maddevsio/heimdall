from aiohttp import web
from app import scan, badge_view



def setup_routes(app):
    app.router.add_get('/', scan)
    app.router.add_get('/badge', badge_view)

if __name__ == '__main__':
    app = web.Application()
    setup_routes(app)
    web.run_app(app)

async def run():
    app = web.Application()
    setup_routes(app)
    return app