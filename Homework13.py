secret = 27
max_attempts = 5
count = 0
guess = 0
print("=" * 42)
print("NUMBER GUESSING GAME")
while count < max_attempts and guess != secret:
    guess = int(input("Your guess: "))
    count = count + 1
    if guess == secret:
        print()
        print(" Correct! You guessed it in", count, "attempt(s)!")
        print("Well done")
    else:
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess

        if diff >= 20:
            print(" Ice cold! You are very far away.")
        elif diff >= 10:
            print(" Cold. Still quite a distance to go.")
        elif diff >= 5:
            print(" Warm! Getting closer...")
        else:
            print(" Hot! Almost there!")
        remaining = max_attempts - count
        if remaining > 0:
            print("Lives left: ", end="")
            for i in range(remaining):
                print("*", end="")
            print()
            print()
if guess != secret:
    print(" Game over! You used all 5 attempts.")
    print("   The secret number was:", secret)