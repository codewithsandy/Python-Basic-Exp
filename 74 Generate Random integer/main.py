import random

def guessGame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger number\n"))
            nguess += 1
        else:
            guess = int(input(f"Enter a smaller number\n"))
            nguess += 1

    print(f"You guessed the number in {nguess} guesses\n")
    return nguess


if __name__ == "__main__":
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual1 = random.randint(a, b)
    print("Player 1's turn\n")
    g1 = guessGame(a, b, actual1)
    print("Player 2's turn\n")
    actual2 = random.randint(a, b)
    g2 = guessGame(a, b, actual2)

    if g1 < g2:
        print("Player 1 won the match!\n")

    elif g1 > g2:
        print("Player 2 won the match!\n")

    else:
        print("Its a Tie!\n")

    print(f"The number for player 1 was {actual1} and for player 2 was {actual2}")

