# import random module
import random
# importing word list from another file
from words_list import words, animals, foods, countries, sports
# import functions from functions file
from functions import create_menu, view_wordlist
# choosing a randon word from our list
random_word = random.choice(words)
# naming file
file_name = "words_list.py"

# Input for user to enter their name
name = input("Enter your name: ").title()

# Greeting 
print(f"Welcome {name} to the word guessing game!!!")

# Starting menu
users_choice = ""

while users_choice != "4":
    users_choice = create_menu()
    if (users_choice == "1"):
        print("start game")
    elif (users_choice == "2"):
        view_wordlist()
    elif (users_choice == "3"):
        print("view previous scores")
    elif (users_choice == "4"):
        continue
    else:
        print("Invalid Input")


print(random_word.title())

if random_word in animals:
    print("Hint: The word is an animal.")
elif random_word in foods:
    print("Hint: The word is a food item.")
elif random_word in countries:
    print("Hint: The word is a country.")
else:
    print("Hint: The word is a sport.")
