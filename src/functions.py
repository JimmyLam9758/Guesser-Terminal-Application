from words_list import animals, foods, countries, sports

def create_menu():
    print("1. Enter 1 start game")
    print("2. Enter 2 to view list of words")
    print("3. Enter 3 to view score")
    print("4. Enter 4 to see how to play")
    print("5. Enter 5 to exit\n")
    choice = input("Enter your selection: ")
    return choice

def view_wordlist():
    print("\nYou have entered '2' - View list of words")
    print(f"\nAnimals = {animals}\n\nCountries = {countries}\n\nFoods = {foods}\n\nSports = {sports}\n")

def view_rules(file_name):
    print("\nYou have entered '4' - How to play")
    with open(file_name, "r") as f:
        rules = f.read()
        print(rules)
    f.close()
