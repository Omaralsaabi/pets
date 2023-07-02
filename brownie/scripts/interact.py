from brownie import PetRegistry


def interact_with_contract():
    contract = PetRegistry[0]  # Assuming you have already deployed the contract

    # Perform interactions with the contract
    contract.addPet(
        "Pet Name",
        "Pet Kind",
        "Pet Breed",
        "Pet Color",
        5,
        "Pet City",
        "Pet Address",
        1234567890,
        "Owner Name",
        "owner@example.com",
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
