#implement one or more functions that collectively test your implementation of shorten thoroughly, 
# each of whose names should begin with test_ so that you can execute your tests with:


import pytest
import sys

from twttr import shorten

def test_main(word):
    assert word('hello world!') == 'hll wrld!'


# Test numbers (invalid input should trigger exit code 1)
def main(word):
    if isinstance(word, (int, float)):
        sys.exit(1)

def test_number():
    with pytest.raises(SystemExit):
        shorten('1')



import sys

def main():
    word = input("Input: ")  # User types in string
    if not word.isalpha():  # Check if the input contains only alphabetic characters
        sys.exit(1)  # Exit with status code 1 for invalid input
    print(shorten(word))  # Print the shortened word with vowels removed
    #Print with the variable remove_v - 'v'

def shorten(word): #def remove_v
    v = "aeiouAEIOU" #v = all vowels
    return "".join([char for char in word if char not in v]) 
#return the text(input) if the char not in v and join them together

if __name__ == "__main__":
    main()






















