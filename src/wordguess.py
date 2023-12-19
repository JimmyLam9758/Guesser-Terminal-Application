# importing modules and functions from other files
import random
from words_list import animals, foods, countries, sports
from functions import create_menu, view_wordlist

# choosing a randon word from our list and getting its length
words = animals + countries + foods + sports
random_word = random.choice(words)
word_length = len(random_word)

# Input for user to enter name and use user input for greeting
name = input("Please enter your name: ").title()
print(f"\nWelcome {name} to the word guessing game!!!\n")

# Game start
def game_start():
    print(f"\nGame has started, begin Guessing!! Your word is {word_length} letters long.\n")
    users_guess = ""
    guesses = 7
    # print correctly guessed characters
    while guesses > 0:
        incorrect_guesses = 0
        for str in random_word:
            if str in users_guess:
                print(str, end = " ")
            else:
                incorrect_guesses += 1
                print("_", end = " ")
        # Print if word was guessed
        if incorrect_guesses == 0:
            print(f"\n\nCongratulations! You got it right with {guesses} guesses remaining. The word was {random_word}.\n")
            break
        # User input for guess
        guess = input("\n\nEnter a letter: ").lower()
        # Make sure guess is 1 only character long and in the english alphabet.
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input. Please only enter 1 letter at a time.")
            continue
        # add guessed letter to their guesses
        users_guess += guess
        # if incorrect guess, lower total guess count, print remaining guesses.
        if guess not in random_word:
            guesses -= 1
            print(f"\nYou have {guesses} guesses remaining.\n")
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
            if guesses == 0:
                print(f"\nBad luck, You have run out of guesses. The word was {random_word}.")

# Starting menu
users_choice = ""
while users_choice != "4":
    users_choice = create_menu()
    if (users_choice == "1"):
        game_start()
    elif (users_choice == "2"):
        view_wordlist()
    elif (users_choice == "3"):
        print("view previous scores")
    elif (users_choice == "4"):
        continue
    else:
        print("Not a valid Input, Please enter a value between 1-4.\n")

print(f"\nThank you {name} for playing! Come back soon!")
