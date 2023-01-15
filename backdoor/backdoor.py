import random

dCardNames = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
dCardValues = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
dSuits = ["Clubs", "Spades", "Diamonds", "Hearts"]
# Build a two dimensional deck with Cards suits and values.
aCards = [['' for i in range(52)] for j in range(3)]
i = 0
n = 0
while i < 13:
    aCards[0][i] = dCardNames[i]
    aCards[0][i + 13] = dCardNames[i]
    aCards[0][i + 26] = dCardNames[i]
    aCards[0][i + 39] = dCardNames[i]
    aCards[1][i] = dSuits[0]
    aCards[1][i + 13] = dSuits[1]
    aCards[1][i + 26] = dSuits[2]
    aCards[1][i + 39] = dSuits[3]
    aCards[2][i] = dCardValues[i]
    aCards[2][i + 13] = dCardValues[i]
    aCards[2][i + 26] = dCardValues[i]
    aCards[2][i + 39] = dCardValues[i]
    i = i + 1
i = 0
# while i < 52:
#     print(aCards[0][i], " ", aCards[1][i], " ", aCards[2][i])
#     i = i + 1

# Shuffling the card pack
for val in aCards:
    random.shuffle(val)
    # shuffling the elements inside the each list

# while i < 52:
#     print(aCards[0][i], " ", aCards[1][i], " ", aCards[2][i])
#     i = i + 1

no_Card = 0
ran_CardName = random.sample(range(0, 52), 10)
ran_CardValue = random.sample(range(0, 52), 10)
ran_Suite = random.sample(range(0, 52), 10)
# Deaing two cards
deal_card = [['' for i in range(10)] for j in range(3)]
while no_Card < 10:
    deal_card[0][no_Card] = aCards[0][ran_CardName[no_Card]]
    deal_card[1][no_Card] = aCards[1][ran_CardValue[no_Card]]
    deal_card[2][no_Card] = aCards[2][ran_Suite[no_Card]]

print(deal_card)

