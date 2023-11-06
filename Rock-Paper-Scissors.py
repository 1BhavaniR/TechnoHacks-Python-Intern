import random

choices = ['rock','paper','scissors']

user_name = str(input("Enter your name : "))
print(f'Welcome {user_name}!!!\n Choose (rock/paper/scissors) ')

while (True):
    user_turn = str(input(f"{user_name}'s turn : "))
    computer_choice = random.choice(choices)
    print(f"Computer's turn:{computer_choice}")
    if((user_turn == 'rock' and computer_choice == 'rock') or (user_turn == 'paper' and computer_choice == 'paper') or (user_turn == 'scissors' and computer_choice == 'scissors')):
        continue
    elif((user_turn == 'rock' and computer_choice == 'scissors') or (user_turn == 'paper' and computer_choice == 'rock') or (user_turn == 'scissors' and computer_choice == 'paper')):
        print(f"{user_name} is Winner!!!")
        break
    else:
        print("Computer is Winner!!!")
        break
