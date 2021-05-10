n = 18
number_of_guesses=1
print("Number of guesses is limited to only 9 times from 1 to 100")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<20:
        print("You enter Less No. Please enter greator no.\n")
    elif guess_number<40:
        print("Please enter greator no.\n")
    elif guess_number<70 or guess_number>=50:
        print("Please enter smaller no.\n")
    elif guess_number<=100:
        print("You enter greator No. Please enter smaller no.\n")
    elif guess_number==50:
        print("YOU WON\n")
        print(number_of_guesses, "number of guesses you took to finish")
        break
    print(9-number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1
if(number_of_guesses>9):
    print("GAME OVER")