import sys


def bisection_guess():
    num_guesses = 0
    low = 0
    high = 100
    ans = (high + low) // 2

    print("Please think of a number between 0 and 100!")
    while True:
        sys.stdout.write("Is your secret number %i?\n"
                         "Enter 'h' to indicate the guess is too high. "
                         "Enter 'l' to indicate the guess is too low. "
                         "Enter 'c' to indicate I guessed correctly. " % ans)
        x = raw_input()

        if x not in "hlc":
            print("Sorry, I did not understand your input.")
            continue

        if x == "c":
            break

        num_guesses += 1
        if x == "l":
            low = ans
        else:
            high = ans
        ans = (high + low) // 2

    print("Game over. Your secret number was: %i" % ans)


bisection_guess()
