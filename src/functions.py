import random
from colored import fg, bg, attr
from words_list import animals, foods, countries, sports

# Function to create start menu
def create_menu():
    print(f"\n{fg('blue')}1. Enter 1 start game")
    print(f"2. Enter 2 to view list of words")
    print(f"3. Enter 3 to see how to play")
    print(f"4. Enter 4 to exit\n{attr('reset')}")
    choice = input(f"{fg('light_yellow')}Enter your selection: {attr('reset')}")
    return choice

# Function to view list of possible words
def view_wordlist():
    print(f"\n{fg('green')}You have entered '2' - View list of words{attr('reset')}")
    print(f"\n{fg('honeydew_2')}Animals = {animals}\n\nCountries = {countries}\n\nFoods = {foods}\n\nSports = {sports}\n{attr('reset')}")

# Function to view how to play the game
def view_rules(file_name):
    print(f"\n{fg('green')}You have entered '4' - How to play\n{attr('reset')}")
    with open(file_name, "r") as f:
        rules = f.read()
        print(f"{fg('honeydew_2')}{rules}{attr('reset')}")
    f.close()

# Function to generate random word and it's length.
def random_word_generator():
    words = animals + countries + foods + sports
    random_word = random.choice(words)
    word_length = len(random_word)
    return random_word, word_length