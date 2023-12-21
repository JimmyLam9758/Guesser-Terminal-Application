# importing modules and functions from other files
import random
import string
import datetime
from colored import fg, attr, bg
from words_list import animals, foods, countries, sports
from functions import create_menu, view_wordlist, view_rules, random_word_generator

# Input for user to enter name and use user input for greeting
while True:
    try:    
        name = input(f"{fg('light_yellow')}Please enter your first name: {attr('reset')}").title()

        if name.isalpha():
            break
        else:
            print(f"\n{fg('red')}Please enter a valid name. No numbers, spaces or special characters.{attr('reset')}\n")

    except KeyboardInterrupt:
        print("\nInput has been interrupted, Exiting ")
        break

print(f"\n{fg('light_yellow')}Welcome {name} to the word guessing game!!!{attr('reset')}")

# Game start loop
def game_start():
    random_word, word_length = random_word_generator()

    print(f"\n{fg('green')}Game has started, begin Guessing!! Your word is {word_length} letters long.{attr('reset')}\n")
    users_guess = ""
    guesses = 7
    set_of_guesses = set()

    # print correctly guessed characters
    while guesses > 0:
        incorrect_guesses = 0
        for str in random_word:
            if str in users_guess:
                print(f"{fg('green')}{str}{attr('reset')}", end = "")
            else:
                incorrect_guesses += 1
                print(f"{fg('sandy_brown')}_{attr('reset')}", end = "")

        # restart function
        def restart():
                while True:
                    start_again = input(f"\n{fg('honeydew_2')}Would you like to play again? Y/N: {attr('reset')}").upper()
                    if start_again == "Y":
                        game_start()
                    elif start_again == "N":
                        print(f"\n{fg('honeydew_2')}Thanks for playing {name}! Come back soon!{attr('reset')}")
                        quit()
                    else:
                        print(f"\n{fg('red')}Invalid Input. Back to main menu.{attr('reset')}")
                        return

        # Print if word was guessed
        if incorrect_guesses == 0:
            print(f"\n\n{fg('green')}Congratulations! You got it right with {guesses} guesses remaining. The word was {random_word}.{attr('reset')}\n")

            # play again option if word was guessed
            restart()
            break

        # User input for guess
        guess = input(f"\n\n{fg('light_yellow')}Enter a letter: {attr('reset')}").lower()
        # users can quit game at any time by typing exit
        if guess == "exit":
            print(f"{fg('honeydew_2')}Thank you for playing! See you again next time.{attr('reset')}")
            quit()
        # Make sure guess is 1 only character long and in the english alphabet.
        if len(guess) != 1 or not guess.isalpha():
            print(f"\n{fg('red')}Invalid Input. Please enter a single letter.{attr('reset')}")
            continue

        users_guess += guess

        # Guess history function
        def guess_history(guess, set_of_guesses, random_word, guesses):
        # if incorrect guess and not in guess history, lower total guess count, print remaining guesses.
            if guess in set_of_guesses:
                print(f"\n{fg('red')}Invalid Input, You have already guessed this letter.{attr('reset')}")
                print(f"{fg('pink_1')}Guess history: {set_of_guesses}{attr('reset')}")
            else:
                set_of_guesses.add(guess)
                if guess in random_word:
                    print(f"\n{fg('pink_1')}Guess history: {set_of_guesses}{attr('reset')}")
                else:
                    guesses -= 1
                    print(f"\n{fg('light_red')}Incorrect guess, You have {guesses} wrong guesses left.{attr('reset')}")
                    print(f"{fg('pink_1')}Guesses history: {set_of_guesses}{attr('reset')}")
            return guesses
        # update and run function
        guesses = guess_history(guess, set_of_guesses, random_word, guesses)   

        # At certain amount of guesses print hint
        if guesses == 4:
                if random_word in animals:
                    print(f"\n{fg('green')}Hint: The word is an animal.{attr('reset')}\n")
                elif random_word in foods:
                    print(f"\n{fg('green')}Hint: The word is a food item.{attr('reset')}\n")
                elif random_word in countries:
                    print(f"\n{fg('green')}Hint: The word is a country.{attr('reset')}\n")
                else:
                    print(f"\n{fg('green')}Hint: The word is a sport.{attr('reset')}\n")

        # Run out of guesses, game over.
        if guesses == 0:
            print(f"\n{fg('red')}Bad luck, You have run out of guesses. The word was {random_word}.{attr('reset')}")
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
        print(f"{fg('honeydew_2')}See you next time!{attr('reset')}")
        quit()
    else:
        print(f"{fg('red')}Not a valid Input, Please enter a value between 1-4.{attr('reset')}\n")

while True:
    game_start()
