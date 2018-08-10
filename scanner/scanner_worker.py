import asyncio
import logging

from app import generate_report


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)


async def scan_github():
    while True:
        log.info('Generating report')
        generate_report()
        log.info('Report generated')
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(scan_github())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
