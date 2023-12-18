import random
# importing word list from another file
from words_list import words, animals, foods, countries
# choosing a randon word from our list
random_word = random.choice(words)

print(random_word)

if random_word in animals:
    print("Hint: The word is an animal.")
elif random_word in foods:
    print("Hint: The word is a food item.")
elif random_word in countries:
    print("Hint: The word is a country.")
else:
    print("Hint: The word is a sport.")

