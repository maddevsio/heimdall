import aioredis
import json
from app import generate_report, root


async def background_report(app):
    try:
        sub = await aioredis.create_redis(('localhost', 6379), loop=app.loop)
        ch, *_ = await sub.subscribe('chan:1')
        async for msg in ch.iter(encoding='utf-8'):
            data = json.loads(msg)
            owner = data.get('owner')
            repo = data.get('repo')
            instance = root.child(f'{owner}/{repo}')
            if not instance.get() or not instance.get('processing'):
                root.child(f'{owner}/{repo}').update({'processing' : True})
                await generate_report(owner, repo)
    except asyncio.CancelledError as e:
        pass
    finally:
        await sub.unsubscribe(ch.name)
        await sub.quit()


async def start_background_tasks(app):
    app['background_report'] = app.loop.create_task(background_report(app))


async def cleanup_background_tasks(app):
    app['background_report'].cancel()
    await app['background_report']
