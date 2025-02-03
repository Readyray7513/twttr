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




