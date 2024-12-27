'''# number guessing game
import random
num = random.randint(1, 10)
guess = None
while guess != num:
    guess = int(input("guess a num between 1 to 10:"))
    #guess = int(guess)

    if guess == num:
        print("congratulation! you won!")
    else:
        print("nope, sorry. try again!")'''
# num guessing game
'''import random
print("\tWelcome to num guessing game.")

def guess_num():
   num = random.randrange(1,10)
   guess = None
   while num != guess:
        guess = int(input("Enter a num between (1-10): "))
        if num == guess:
            print("you Win!")
            choice = input("Do you want to play again(Yes/No): ")
            if choice.lower() == "yes":
               guess_num()
            else:
                quit()   
        else:
            print("Try again.")

guess_num()'''
import random
import tkinter as tk
from tkinter import messagebox

def guess_num():
    # Generate random number between 1 and 10
    num = random.randrange(1, 11)
    
    # Create the window
    app = tk.Tk()
    app.title("Num Guessing Game")

    # Function to handle the guess check
    def check_guess():
        try:
            guess = int(guess_entry.get())  # Get the user's guess
            if guess < 1 or guess > 10:
                messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 10.")
            elif guess == num:
                # Ask if the user wants to play again after winning
                result = messagebox.askyesno("You Win!", "Congratulations, you guessed the number! Would you like to play again?")
                if result:
                    app.destroy()  # Close the current window to restart the game
                    guess_num()  # Restart the game by calling the function again
                else:
                    app.destroy()  # Close the game window
            else:
                messagebox.showinfo("Try again", "Wrong guess. Try again!")
                guess_entry.delete(0, tk.END)  # Clear the entry field for a new guess
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    # UI elements
    tk.Label(app, text="Guess a number (1-10):").grid(row=0, column=0, padx=10, pady=10)
    guess_entry = tk.Entry(app)  # Create entry field for user input
    guess_entry.grid(row=0, column=1, padx=10, pady=10)

    predict_btn = tk.Button(app, text="Predict", command=check_guess)  # Button to trigger the guess check
    predict_btn.grid(row=1, column=0, columnspan=2, pady=20)

    # Start the Tkinter event loop
    app.mainloop()

# Start the game
guess_num()
