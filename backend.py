import numpy as np
def guess_numbers():
    num = np.random.randint(100)
    attempt = np.random.randint(5,10)
    guess_number = 1
    print("Number of guesses is limited to only ",attempt," Time")
    print("Guess the Number:")
    while (guess_number<=attempt):
        inp =int(input())
        if inp < num:
            print("You Entered Less Number. \n")
            print(attempt-guess_number,"no. of guesses left")
            print("Try again. \n")
        elif inp > num:
            print("You Entered greater number. \n")
            print(attempt-guess_number,"no. of guesses left")
            print("Try Again.")
        else:
            print("You WON. \n")
            print("You took",guess_number," attempt to guess the Number")
            break
        #print(attempt-guess_number,"no. of guesses left")
        guess_number = guess_number+1

    if guess_number>attempt:
        print("You took more time to guess")

    print()
    print("Game is Restarted")
    guess_numbers()

guess_numbers()