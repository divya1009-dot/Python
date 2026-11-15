import random
num=str(random.randint(0,9))
print("I am genarating a number from 0,9 and you try to guess it")
while True:
    guess=input("guess the lucky number ")
    if guess==num:
        print("you have won the game")
        print("The number was",num)
        break
    else:
        print("try again")
