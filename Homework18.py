import random
import math
print("===== RANDOM FUN CALCULATOR =====")
luck_num = random.randint(1, 10)
print("Your lucky number is:", luck_num)
fun_choices = ["Play a game", "Solve a puzzle", "Read a story", "Draw something"]
random_act= random.choice(fun_choices)
print("Random activity for today:", random_act)
print("\nGuess the secret number from 1 to 5!")
secret_num = random.randint(1, 5)
while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_num:
        print("horaaayy! You guessed the number.")
        break
    else:
        print("Wrong guess")
dec_num = float(input("\nEnter a decimal number: "))
print("Ceiling value:", math.ceil(dec_num))
print("Floor value:", math.floor(dec_num))
x = 10
y = -5
print("x copysign y is : ", math.copysign(x, y))
neg_num = int(input("Enter a negative number: "))
print("Absolute value:", math.fabs(neg_num))
num1 = int(input("Enter first number for GCD: "))
num2 = int(input("Enter second number for GCD: "))
print("GCD is:", math.gcd(num1, num2))
print("\n===== FUN CALCULATOR SUMMARY =====")
print("Lucky Number:", luck_num)
print("Random Activity:", random_act)
print("Secret Number:", secret_num)
print("==================================")