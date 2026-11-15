import random
print("we are playing rock paper scissors togather")
while True:
    user_choice=input("enter what you picked").strip().lower()
    pos_choice=["rock", 'paper', 'scissors']
    comp_choice=random.choice(pos_choice)
    print(f"I chose {comp_choice} and you chose {user_choice}")
    if user_choice==comp_choice:
        print("Its a Tie")
    elif user_choice=="rock":
        if comp_choice=='paper':
            print('paper covers rock, I win!')
        else:
            print("rock smashes scissors, I lose")
    elif user_choice=='scissors':
        if comp_choice=='paper':
            print("scissors cuts paper, I lose")
        else:
            print("rock smashes scissors, I win!")
    elif user_choice=='paper':
        if comp_choice=='rock':
            print("paper covers rock, I lose")
        else:
            print('scissor cuts paper, I win!')
    play=input("do you want to play again? y/n ").strip().lower()
    if play=="n":
        break