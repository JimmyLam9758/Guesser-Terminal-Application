import pytest

# # TEST 1 testing that length is equal to amount of char in word, EXPECTED OUTCOME - PASS
# word = "penguin"
# length = 7

# # TEST 2 testing that length of the word cannot be zero, EXPECTED OUTCOME = FAIL
# word = ""
# length = 1

# # TEST 3 testing if length != to chars in word it doesn't pass. EXPECTED OUTCOME = FAIL
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

