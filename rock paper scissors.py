import random
while True:
    user_action=input("enter a choice(rock,paper,scissors): ")
    possible_actions=["rock","paper","scissors"]
    computer_action=random.choice(possible_actions)
    print(f"\nyou chose {user_action} computer chose {computer_action}.\n")
if user_action==computer_action:
    print(f"both players selected {user_action}. It's a tie!")
elif user_action=="rock":
    if computer_action=="scissors":
        print("rock crushes scissors! You win!")
    else:
        print("paper covers rock! You lose.")
elif user_action=="paper":
    if computer_action=="rock":
        print("paper covers rock! You win!")
    else:
        print("scissors cuts paper! You lose.")
elif user_action=="scissors":
    if computer_action=="paper":
        print("scissors cuts paper! You win!")
    else:
        print("rock crushes scissors! You lose.")
print("do you want to play again? (yes/no)")
play_again=input()
if play_again.lower()!="yes":
    print("thank you for playing!")
print("goodbye!")