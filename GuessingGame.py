import random
#from random import randint


for i in range(1,5):
    gnum = int(input("Enter any number from 0 to 10 : "))

    rnum = random.randint(1, 10)
    # rnum = random.random()*100   # -> 0 to 100

    if gnum == rnum:
        print("Won")
    else:
        print("Lost")
        print("Random Number was", rnum)
