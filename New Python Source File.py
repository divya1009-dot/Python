print("===NUmber Guessing game===")
secret=29
count=0
while count<5 or guess!=secret:
    guess=int(input("Enter a number which you think is right"))
    if guess==int(secret):
        print("you have won!")
    else:
        print("the answer was wrong")
        if guess < secret:
            print("you have to guess higher")
        else:
            print("you have to guess lower")