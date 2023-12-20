# importing modules and functions from other files
import random
from words_list import animals, foods, countries, sports
from functions import create_menu, view_wordlist, view_rules, random_word_generator

# Input for user to enter name and use user input for greeting
while True:
    try:    
        name = input("Please enter your first name: ").title()

        if name.isalpha():
            break
        else:
            print("\nPlease enter a valid name. No numbers, spaces or special characters.\n")

    except KeyboardInterrupt:
        print("\nInput has been interrupted, Exiting ")
        break

print(f"\nWelcome {name} to the word guessing game!!!")

# Game start loop
def game_start():
    random_word, word_length = random_word_generator()

    print(f"\nGame has started, begin Guessing!! Your word is {word_length} letters long.\n")
    users_guess = ""
    guesses = 7
    set_of_guesses = set()

    # print correctly guessed characters
    while guesses > 0:
        incorrect_guesses = 0
        for str in random_word:
            if str in users_guess:
                print(str, end = "")
            else:
                incorrect_guesses += 1
                print("_", end = "")

        # restart function
        def restart():
                while True:
                    start_again = input("\nWould you like to play again? Y/N: ").upper()
                    if start_again == "Y":
                        game_start()
                    elif start_again == "N":
                        print(f"\nThanks for playing {name}! Come back soon!")
                        quit()
                    else:
                        print("\nInvalid Input. Back to main menu.")
                        return

        # Print if word was guessed
        if incorrect_guesses == 0:
            print(f"\n\nCongratulations! You got it right with {guesses} guesses remaining. The word was {random_word}.\n")
            # play again option if word was guessed
            restart()
            break

        # User input for guess
        guess = input("\n\nEnter a letter: ").lower()

        # Make sure guess is 1 only character long and in the english alphabet.
        if len(guess) != 1 or not guess.isalpha():
            print("\nInvalid Input. Please enter a single letter.")
            continue

        users_guess += guess

        # Guess history
        # if incorrect guess and not in guess history, lower total guess count, print remaining guesses.
        if guess not in random_word and guess in set_of_guesses:
            print("\nYou have already guessed this letter.")
            print(f"You have {guesses} guesses remaining.")
            print(f"Guesses so far: {set_of_guesses}")
        elif guess in random_word and guess in set_of_guesses:
            print("\nYou have already guessed this letter.")
            print(f"You have {guesses} guesses remaining.")
            print(f"Guesses so far: {set_of_guesses}")
        elif guess in random_word and guess not in set_of_guesses:
            set_of_guesses.add(guess)
            print(f"You have {guesses} guesses remaining.")
            print(f"Guesses so far: {set_of_guesses}")
        else:
            set_of_guesses.add(guess)
            guesses -= 1
            print(f"You have {guesses} guesses remaining.")
            print(f"Guesses so far: {set_of_guesses}")

        # At certain amount of guesses print hint
        if guesses == 4:
                if random_word in animals:
                    print("\nHint: The word is an animal.\n")
                elif random_word in foods:
                    print("\nHint: The word is a food item.\n")
                elif random_word in countries:
                    print("\nHint: The word is a country.\n")
                else:
                    print("\nHint: The word is a sport.\n")

        # Run out of guesses, game over.
        if guesses == 0:
            print(f"\nBad luck, You have run out of guesses. The word was {random_word}.")
            restart()
            break

# Starting menu
file_name = "rules.txt"
users_choice = ""
while users_choice != "4":
    users_choice = create_menu()
    if (users_choice == "1"):
        game_start()
    elif (users_choice == "2"):
        view_wordlist()
    elif(users_choice == "3"):
        view_rules(file_name)
    elif (users_choice == "4"):
        print("See you next time!")
        quit()
    else:
        print("Not a valid Input, Please enter a value between 1-4.\n")

while True:
    game_start()
