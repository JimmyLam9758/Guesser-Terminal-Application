import pytest

# # TEST 1 testing that length is equal to amount of char in word, EXPECTED OUTCOME - PASS
# word = "penguin"
# length = 7

# # TEST 2 testing that length of the word cannot be zero, EXPECTED OUTCOME = FAIL
# word = ""
# length = 1

# # TEST 3 testing if length != to chars in word. EXPECTED OUTCOME = FAIL
# word = "soup"
# length = 3

# parametrize tests to run tests all together
@pytest.mark.parametrize("word, length", [("penguin", 7), ("", 0), ("soup", 3)])
def test_random_word_generator(word, length):
    assert isinstance(word, str)
    assert isinstance(length, int)
    if length == 0:
        pytest.fail("Length of word can't be zero")
    elif length != len(word):
        pytest.fail("Length of word is not equal to length")

# # TEST 1 testing to see outcome if correct letter is guessed and has not been guessed before. EXPECTED OUTCOME = PASS
# guess = "f"
# set_of_guesses = set()
# random_word = fish
# guesses = 7
# expected = 7

# # TEST 2 testing to see for outcome of incorrect guess. EXPECTED OUTCOME = PASS
# guess = "f"
# set_of_guesses = {"f"}
# random_word = fish
# guesses = 6
# expected = 6

# # TEST 3 testing to see outcome for duplicate guess. EXPECTED OUTCOME = FAIL
# guesses should not go down if guess is already in set_of_guesses
# guess = "r"
# set_of_guesses = {"f", "r"}
# random_word = fish
# guesses = 5
# expected = 6

@pytest.mark.parametrize("guess, set_of_guesses, random_word, guesses, expected", [
    ("f", {"f"}, "fish", 7, 7),
    ("r", {"f", "r"}, "fish", 6, 6),
    ("r", {"f", "r"}, "fish", 5, 6)])
def test_guess_history(guess, set_of_guesses, random_word, guesses, expected):
    assert guesses == expected