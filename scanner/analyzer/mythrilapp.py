import logging
from mythril.mythril import Mythril

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)

def mythril_scanner(smart_contract):
    logging.info(f'[{smart_contract}] Mythril scanner')
    mythril = Mythril(
        solv=None, dynld=False, solc_args=None
    )
    address, _ = mythril.load_from_solidity([smart_contract, ])
    logging.info(f'[{smart_contract}] address={address}')

    report = mythril.fire_lasers(
        strategy='dfs',
        address=address,
        modules=[],
        verbose_report=False,
        max_depth=22,
        execution_timeout=600
    )
    logging.info(f'[{smart_contract}] report={report.as_json()}')
    return report.as_json()
