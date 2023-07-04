from brownie import PetRegistry
from scripts.helpful_scripts import get_account


def interact_with_contract():
    print("Interacting with the contract")
    account = get_account()
    contract = PetRegistry[0]  # Assuming you have already deployed the contract

    # Perform interactions with the contract
    contract.addPet(
        "Budran",
        "husky",
        "husky",
        "black",
        25,
        "Amman",
        "Alsowayfiah",
        7777777777,
        "Omar",
        "budran.nigga@gmail.com",
        {"from": account},
    )

    pet = contract.getPet(0)
    print("Pet Details:")
    print("Name:", pet[0])
    print("Kind:", pet[1])
    print("Breed:", pet[2])
    print("Color:", pet[3])
    print("Age:", pet[4])
    print("City:", pet[5])
    print("Address:", pet[6])
    print("Phone:", pet[7])
    print("Owner Name:", pet[8])
    print("Email:", pet[9])


def main():
    interact_with_contract()
