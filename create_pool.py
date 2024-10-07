from pathlib import Path

from sui_brownie import sui_brownie

sui_project = sui_brownie.SuiProject(project_path=Path(__file__).parent, network="sui-mainnet")
sui_project.active_account("MAIN")

pacakge_id = "0xe030c518163b0f4ed043243bebf85c16743063d98efda5e642a176308c0a54fb"
escrow_reward = "0xa8371f3bc97b4ed56a35d7bb6d0ec543303f60b5f6721d16833c3d639d7dd30d"
sui_object = "0xf5f8a63dca4df11b8881b844ca7be98e9a9b934921c88b4331ccb79fb30f1751"
proposal = "0x702347c1ab4905fbd311198cb6805c30295a13f8c2a429db2efeaa61078b486d"

governance_info = "0x79d7106ea18373fc7542b0849d5ebefc3a9daf8b664a4f82d9b35bbd0c22042d"
storage = "0xe5a189b1858b207f2cf8c05a09d75bae4271c7a9a8f84a8c199c6896dc7c37e6"


def load_pacakge():
    return sui_brownie.SuiPackage(
        package_id="0xe030c518163b0f4ed043243bebf85c16743063d98efda5e642a176308c0a54fb",
        package_name="Proposal"
    )


def create_proposal():
    pacakge = load_pacakge()
    result = pacakge.proposal.create_proposal(
        governance_info,
        escrow_reward,
        sui_object
    )
    print(result)


def vote_porposal():
    pacakge = load_pacakge()
    result = pacakge.proposal.vote_porposal(
        governance_info,
        storage,
        escrow_reward,
        proposal
    )
    print(result)


if __name__ == "__main__":
    # create_proposal()
    vote_porposal()
