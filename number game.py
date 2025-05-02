import random
playing = True
number = str(random.randint(10,20))
print("I wll generate a number from 10 to 20. You have to guess")
print("the game ends once you guess it")
while playing:
    guess=(input("enter your guess: "))
    if number==guess:
        print("your guess is correct. You win the game")
        break
    else:
        print("wrong answer. Try again")