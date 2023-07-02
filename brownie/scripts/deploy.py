from brownie import PetRegistry, accounts, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_pet_registry():
    account = get_account()
    # pass the price feed address to our smart contract
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        # if we are on a local environment, we need to deploy mocks
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks...")
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

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
