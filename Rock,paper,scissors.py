import random

exit = False
user_points = 0
computer_points = 0

while not exit:
    options = ["Rock", "Paper", "Scissors"]
    user_input = input("Choose Rock, Paper, Scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended!")
        exit = True

    elif user_input == "Rock":
        if computer_input == "Rock":
            print("Your input is Rock")
            print("computer input is Rock")
            print("It's a tie!")
        if computer_input == "Paper":
            print("Your input is Rock")
            print("computer input is Paper")
            print("computer win!")
            computer_points += 1
            print(computer_points)
        if computer_input == "Scissors":
            print("Your input is Rock")
            print("computer input is Scissors")
            print("you win!")
            user_points += 1
            print(user_points)
        continue
    elif user_input == "Paper":
        if computer_input == "Rock":
            print("Your input is Paper")
            print("computer input is Rock")
            print("you win!")
            user_points += 1
            print(user_points)
        if computer_input == "Paper":
            print("Your input is Paper")
            print("computer input is Paper")
            print("It's a tie!")
        if computer_input == "Scissors":
            print("Your input is Paper")
            print("computer input is Scissors")
            print("computer win!")
            computer_points += 1
            print(computer_points)
        continue
    elif user_input == "Scissors":
        if computer_input == "Rock":
            print("Your input is Scissors")
            print("computer input is Rock")
            print("computer win!")
            computer_points += 1
            print(computer_points)
        if computer_input == "Paper":
            print("Your input is Scissors")
            print("computer input is Paper")
            print("you win!")
            user_points += 1
            print(user_points)
        if computer_input == "Scissors":
            print("Your input is Paper")
            print("computer input is Scissors")
            print("It's a tie!")
        continue
    else:
        print("Invalid input")
        continue








