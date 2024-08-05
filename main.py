import tkinter as tk
import numpy as np

# Function to initialize the game
def initialize_game():
    global num, attempt, guess_number
    num = np.random.randint(100)
    attempt = np.random.randint(5, 10)
    guess_number = 1
    info_label.config(text=f"Number of guesses is limited to only {attempt} times.\nGuess the Number:")
    result_label.config(text="")
    input_entry.delete(0, tk.END)
    input_entry.config(state=tk.NORMAL)
    guess_button.config(state=tk.NORMAL)

# Function to check the guess
def check_guess():
    global guess_number
    try:
        inp = int(input_entry.get())
        if inp < num:
            result_label.config(text=f"You entered a smaller number.\n{attempt - guess_number} guesses left.\nTry again.")
        elif inp > num:
            result_label.config(text=f"You entered a larger number.\n{attempt - guess_number} guesses left.\nTry again.")
        else:
            result_label.config(text=f"You WON!\nYou took {guess_number} attempts to guess the number.")
            input_entry.config(state=tk.DISABLED)
            guess_button.config(state=tk.DISABLED)
            reset_button.pack_forget()
            restart_button.pack(pady=20)
            return
        guess_number += 1
        input_entry.delete(0, tk.END)
        if guess_number > attempt:
            result_label.config(text=f"You took too many guesses. You lost! \n The Number is {num}")
            input_entry.config(state=tk.DISABLED)
            guess_button.config(state=tk.DISABLED)

            reset_button.pack_forget()
            restart_button.pack(pady=20)
            
            
            
            
    except ValueError:
        result_label.config(text="Please enter a valid number.")


# Functon for Disappearing and Appearing Button
def disappearbutton():
    restart_button.pack_forget()
    quit_button.pack_forget()
    reset_button.pack(pady=10)

# Function for quitting the Windows
def quit_window():
    root.destroy()

# Function for holding 2 function in 1 function
def multiple():
    disappearbutton()
    initialize_game()


# Create main window
root = tk.Tk()
root.title("Number Guessing Game")
root.configure(bg="lightblue")


# Create widgets
info_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label = tk.Label(root, text="", font=("Helvetica", 12))
input_entry = tk.Entry(root, font=("Helvetica", 14))
guess_button = tk.Button(root, text="Guess",bg="#4682B4", font=("Helvetica", 14), command=check_guess)
reset_button = tk.Button(root, text="Reset Game", bg="orange", font=("Helvetica", 14), command=initialize_game)
restart_button = tk.Button(root, text="Restart Game",bg="lightgreen", font=("Helvetica", 14), command=multiple)
quit_button = tk.Button(root, text="Quit Game",bg="red", font=("Helvetica", 14), command=quit_window)


# Place widgets
info_label.pack(pady=10)
input_entry.pack(pady=10)
guess_button.pack(pady=10)
result_label.pack(pady=10)
reset_button.pack(pady=10)
quit_button.pack(pady=20)


# Initialize game
initialize_game()

# Connect The Enter Key with Guess Button
root.bind("<Return>",lambda event:guess_button.invoke())

# Start the Tkinter event loop
root.mainloop()