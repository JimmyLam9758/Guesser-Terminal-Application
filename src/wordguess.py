# import random module
import random
# importing word list from word list file
from words_list import words, animals, foods, countries, sports
# import functions from functions file
from functions import create_menu, view_wordlist
# choosing a randon word from our list and getting its length
random_word = random.choice(words)
word_length = len(random_word)
# naming file
file_name = "words_list.py"

# Input for user to enter their name
name = input("Enter your name: ").title()
# Greeting 
print(f"Welcome {name} to the word guessing game!!!")

# Game start
def game_start():
    print(f"Game has started, begin Guessing!! Your word is {word_length} letters long.")
    users_guess = ""
    guesses = 7
    # Hints
    if random_word in animals:
        print("Hint: The word is an animal.")
    elif random_word in foods:
        print("Hint: The word is a food item.")
    elif random_word in countries:
        print("Hint: The word is a country.")
    else:
        print("Hint: The word is a sport.")
    # 
    while guesses > 0:
        incorrect_guesses = 0
        for str in random_word:
            if str in users_guess:
                print(str, end = " ")
            else:
                incorrect_guesses += 1
                print("_", end = " ")

        if incorrect_guesses == 0:
            print(f"\nCongratulations! You guessed the word correctly. The word was {random_word}.")
            break
        # user guess input
        guess = input("\nEnter your guess: ").lower()
        users_guess += guess
        # Incorrect guesses output
        if guess not in random_word:
            guesses -= 1
            print(f"Incorrect, You have {guesses} guesses remaining.")
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

