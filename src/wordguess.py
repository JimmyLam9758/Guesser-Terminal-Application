import random
# importing word list from another file
from words_list import words, animals, foods, countries
# choosing a randon word from our list
random_word = random.choice(words)

print(random_word)

