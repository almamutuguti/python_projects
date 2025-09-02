game_choices = ["Rock", "Paper", "Scissors"]
users_choice = int(input("What do you choose?Type 0 for rock 1 for paper and 2 for scissors.\n"))
if users_choice <=0 or users_choice >=2:
    print(f"You chose: {game_choices[users_choice]}")
else:
    print("Try again")

import random
computers_choice = random.randint(0, 2)
print(f"Computer chose: {game_choices[computers_choice]}")

if users_choice >=3 or users_choice <0:
    print("You typed an invalid number.You lose!")
elif computers_choice == 2 and users_choice == 0:
    print("You win!")
elif computers_choice > users_choice:
    print("You lose!")
elif computers_choice < users_choice:
    print("You win!")
elif computers_choice == 0 and users_choice == 2:
    print("You lose!")
elif computers_choice == users_choice:
    print("It's a draw")
elif computers_choice == 0 and users_choice == 2:
    print("You lose!")
else:
    print("Try again")
