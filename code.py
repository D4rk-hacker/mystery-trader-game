import random
import time

print('*' * 10, 'Mystery Trader Game', '*' * 10)

# Player cards
dragon = {
    "Health": 5,
    "Power": 5
}

elf = {
    "Health": 7,
    "Power": 3
}

orc = {
    "Health": 3,
    "Power": 3
}

# Game
cards = [dragon, elf, orc]

print("Your cards:")
print("Dragon", dragon)
print("Elf", elf)
print("Orc", orc)

card = input("Your turn! Which card do you want to play? ")
card_comp = random.choice(cards)

if card == "Dragon":
    print("You chose:", dragon)
    card = dragon
elif card == "Elf":
    print("You chose:", elf)
    card = elf
elif card == "Orc":
    print("You chose:", orc)
    card = orc

time.sleep(1)
print("Opponent's turn:", card_comp)

while True:
    print("You attack!")
    time.sleep(2)

    if card["Power"] >= card_comp["Health"]:
        print("You defeated your opponent!")
        break

    if card["Power"] < card_comp["Health"]:
        print("You managed to injure your opponent!")
        card_comp["Health"] -= card["Power"]
        print(card_comp)

        print("Opponent's turn!")
        time.sleep(2)

        if card_comp["Power"] >= card["Health"]:
            print("You lost!")
            break
        elif card_comp["Power"] < card["Health"]:
            print("Your opponent injured you!")
            card["Health"] -= card_comp["Power"]
            print(card)
