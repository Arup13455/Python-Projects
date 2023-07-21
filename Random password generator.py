# Ask user if they want to generate password or not.
# If yes, ask for password length.
# Generate pass word
# Print password
# If initial response is no, then exit program
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*")


def generate_password():
    password_length = int(input("How long do you want to create your password?"))
    random.shuffle(characters)

    password = []
    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Do you want to generate a password? (Yes/No):")
if option == "Yes":
    generate_password()
elif option == "No":
    print("program ended")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()
