import random,string

index = [i for i in range(26)]
suffIndex = random.shuffle(index)

apha = list(string.ascii_lowercase)


word = input("enter stirng to encrpt :")

for i in word :
    print(i ,apha.index(i) )


#print(index,suffIndex,apha)