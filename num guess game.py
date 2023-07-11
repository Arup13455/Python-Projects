# number guessing game
import random
num = random.randint(1, 10)
guess = None
while guess != num:
    guess = input("guess a num between 1 to 10:")
    guess = int(guess)

    if guess == num:
        print("congratulation! you won!")
        break
    else:
        print("nope, sorry. try again!")
