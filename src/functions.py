import random
from words_list import animals, foods, countries, sports

# Function to create start menu
def create_menu():
    print("\n1. Enter 1 start game")
    print("2. Enter 2 to view list of words")
    print("3. Enter 3 to view previous scores")
    print("4. Enter 4 to see how to play")
    print("5. Enter 5 to exit\n")
    choice = input("Enter your selection: ")
    return choice

# Function to view list of possible words
def view_wordlist():
    print("\nYou have entered '2' - View list of words")
    print(f"\nAnimals = {animals}\n\nCountries = {countries}\n\nFoods = {foods}\n\nSports = {sports}\n")

# Function to view how to play the game
def view_rules(file_name):
    print("\nYou have entered '4' - How to play\n")
    with open(file_name, "r") as f:
        rules = f.read()
        print(rules)
    f.close()

# Function to generate random word and it's length.
def random_word_generator():
    words = animals + countries + foods + sports
    random_word = random.choice(words)
    word_length = len(random_word)
    return random_word, word_length