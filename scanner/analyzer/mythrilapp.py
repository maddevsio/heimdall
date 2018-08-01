from mythril.analysis.symbolic import SymExecWrapper
from mythril.analysis.security import fire_lasers
from mythril.analysis.report import Report 
from mythril.ether.soliditycontract import SolidityContract

ADDRESS = "0x0000000000000000000000000000000000000000"

def mythril_scanner(contract_file):
    contract = SolidityContract(contract_file)
    sym = SymExecWrapper(contract, address=ADDRESS, strategy="dfs")
    issues = fire_lasers(sym)
    report = Report()
    for issue in issues:                                           
        issue.filename = "test-filename.sol"
        report.append_issue(issue)    
    return report
