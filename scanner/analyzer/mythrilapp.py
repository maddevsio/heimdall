from mythril.mythril import Mythril
from mythril.analysis.report import Report 



def mythril_scanner(contract_file):
    mythril = Mythril(
        solv=None, dynld=False, solc_args=None
    )
    address, _ = mythril.load_from_solidity([contract_file, ])

    return mythril.fire_lasers(
        strategy='dfs',
        address=address,
        modules=[],
        verbose_report=False,
        max_depth=22,
        execution_timeout=600
    )