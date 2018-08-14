from mythril.mythril import Mythril


def mythril_scanner(smart_contracts):
    mythril = Mythril(
        solv=None, dynld=False, solc_args=None
    )
    address, _ = mythril.load_from_solidity(smart_contracts)

    return mythril.fire_lasers(
        strategy='dfs',
        address=address,
        modules=[],
        verbose_report=False,
        max_depth=22,
        execution_timeout=600
    )