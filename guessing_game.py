import random


def guess_num():

    random_number = random.randint(0, 15)

    guesses = 5
    found = True

    num_already_guessed = []

    while guesses > 0:
        your_guess = int(input("Guess a number between 1 and 15, what number am I: "))

        if your_guess != random_number:
            num_already_guessed.append(your_guess)

        if your_guess == random_number:
            found = True
            print("WINNER WINNER CHICKEN DINNER! that's right the number was {}".format(random_number))
        elif your_guess > random_number:
            print("Not quite, go lower")
        elif your_guess < random_number:
            print("Not quite, go higher")

        guesses -= 1
        print("You have {} guesses left".format(guesses))
        print(num_already_guessed)

    print("Aww mann the number I was thinking of was the number " + str(random_number))


guess_num()


play_again = input("Do you want to try again? ")

if play_again.lower() != "no":
    guess_num()
else:
    print("Thanks for playing, better luck next time")



# Thanks for watching, please subscribe below  :) take care
