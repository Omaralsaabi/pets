from brownie import PetRegistry, accounts, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_pet_registry():
    account = get_account()
    pet_registry = PetRegistry.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )  # publish_source=True is used to verify the contract on Etherscan when dealing with non-local networks
    print(f"Contract deployed to {pet_registry.address}")
    return pet_registry


def main():
    deploy_pet_registry()


if __name__ == "__main__":
    main()
