import random
# importing word list from another file
from words_list import words, animals, foods, countries
# choosing a randon word from our list
random_word = random.choice(words)

name = input("Enter your name: ").title()

print(f"Welcome {name} to the word guessing game!!!")

print(random_word.title())

if random_word in animals:
    print("Hint: The word is an animal.")
elif random_word in foods:
    print("Hint: The word is a food item.")
elif random_word in countries:
    print("Hint: The word is a country.")
else:
    print("Hint: The word is a sport.")

def create_menu():
    print("1. Enter 1 start game")
    print("2. Enter 2 to view word lists")
    print("3. Enter 3 to view score")
    print("4. Enter 4 to exit")
    choice = input("Enter your selection: ")
    return choice