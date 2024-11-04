from pathlib import Path

from sui_brownie import sui_brownie

sui_project = sui_brownie.SuiProject(project_path=Path(__file__).parent, network="sui-mainnet")
sui_project.active_account("MAIN")

pacakge_id = "0x9fe4ad5393f2096bf36ebf5c459311ec79385e0ab899aa5de7ba6c3a54b66106"
escrow_reward = "0x47364e57f86cafb709e587e15e48e7024b677bfbb8655afbe8aa438827b1c3d8"
sui_object = "0xf534b2b7de0d908bd7520f32f6de0cb568191929f316e9ba646fd45946e51cba"
proposal = "0xd9b5e52d196a19ec87733be6fd204bb4020a285a7d0d34aada7ea32e4e7b6df6"

governance_info = "0x79d7106ea18373fc7542b0849d5ebefc3a9daf8b664a4f82d9b35bbd0c22042d"
storage = "0xe5a189b1858b207f2cf8c05a09d75bae4271c7a9a8f84a8c199c6896dc7c37e6"


def load_pacakge():
    return sui_brownie.SuiPackage(
        package_id=pacakge_id,
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
