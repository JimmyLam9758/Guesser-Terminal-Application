from words_list import animals, foods, countries, sports

def create_menu():
    print("1. Enter 1 start game")
    print("2. Enter 2 to view list of words")
    print("3. Enter 3 to view score")
    print("4. Enter 4 to exit")
    choice = input("Enter your selection: ")
    return choice

def view_wordlist():
    print("You have entered '2' - View list of words")
    print(f"\nAnimals = {animals}\n\nCountries = {countries}\n\nFoods = {foods}\n\nSports = {sports}\n")