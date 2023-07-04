from brownie import PetRegistry
from scripts.helpful_scripts import get_account


account = get_account()
contract = PetRegistry[0]


# def interact_with_contract():
#     print("Interacting with the contract")
#     account = get_account()
#     contract = PetRegistry[0]  # Assuming you have already deployed the contract

#     # Perform interactions with the contract
#     contract.addPet(
#         input("Name: "),
#         input("Kind: "),
#         input("Breed: "),
#         input("Color: "),
#         int(input("Age: ")),
#         input("City: "),
#         input("Address: "),
#         input("Phone: "),
#         input("Owner Name: "),
#         input("Email: "),
#         {"from": account},
#     )

#     pet = contract.getPet(0)
#     print("Pet Details:")
#     print("Name:", pet[0])
#     print("Kind:", pet[1])
#     print("Breed:", pet[2])
#     print("Color:", pet[3])
#     print("Age:", pet[4])
#     print("City:", pet[5])
#     print("Address:", pet[6])
#     print("Phone:", pet[7])
#     print("Owner Name:", pet[8])
#     print("Email:", pet[9])


def addPet():
    contract.addPet(
        input("Name: "),
        input("Kind: "),
        input("Breed: "),
        input("Color: "),
        input("Age: "),
        input("City: "),
        input("Address: "),
        input("Phone: "),
        input("Owner Name: "),
        input("Email: "),
        {"from": account},
    )


def getPet():
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
    # interact_with_contract()
    # addPet()
    getPet()
