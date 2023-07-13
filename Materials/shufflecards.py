import random


dCardNames = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
dCardValues = ['2','3','4','5','6','7','8','9','10','11','12','13','14']
dSuits = ["Clubs","Spades","Diamonds","Hearts"]
# Build a two dimensional deck with Cards suits and values.
aCards =  [['' for i in range(52)] for j in range(3)]
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
#     print (aCards[0][i], " ", aCards[1][i], " ", aCards[2][i])
#     i = i + 1

#Shuffling the inner list elemenets inside the list
for val in aCards :
    random.shuffle(val)

# while i < 52:
#     print (aCards[0][i], " ", aCards[1][i], " ", aCards[2][i])
#     i = i + 1

ran_CardName = random.sample(range(0,52),10) # Getting random numbers to use as index for dCardName list
ran_CardValue = random.sample(range(0,52),10) # Getting random numbers to use as index for dCardValue list
ran_Suite = random.sample(range(0,52),10) # Getting random number to use as index for dSuite list

c = 0 # use it as counter to iterate thorough loop

dealt_Cards= [['' for i in range(10)] for j in range(3)]

#Dealing ten shuffled random cards.
while c < 10 :

    dealt_Cards[0][c]= aCards[0][ran_CardName[c]]
    dealt_Cards[1][c]= aCards[1][ran_CardValue[c]]
    dealt_Cards[2][c]= aCards[2][ran_Suite[c]]
    c += 1
#print(dealt_Cards)
#spliting the dealt cards into two.
hand_One = [dealt_Cards[0][0:5],dealt_Cards[1][0:5],dealt_Cards[2][0:5]]
hand_Two = [dealt_Cards[0][5:10],dealt_Cards[1][5:10],dealt_Cards[2][5:10]]

x= 0
while x < 5 :
    print("hand one ",hand_One[0][x], " ", hand_One[1][x], " ", hand_One[2][x])
    print("hand two ",hand_Two[0][x], " ", hand_Two[1][x], " ", hand_Two[2][x])
    x+=1
    