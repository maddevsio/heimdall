import asyncio
import logging

from app import generate_report, root

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)

async def scan_github():
    while True:
        log.info('Generating report')
        catalog = root.get()
        for owner, node in catalog.items():
            for repo, _ in node.items():
                generate_report(owner, repo)
        log.info('Report generated')
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(scan_github())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()
