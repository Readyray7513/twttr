def main():
    text = input("Input: ")#User types in string
    print("", remove_v(text))#Print with the variable remove_v - 'v'


def remove_v(text): #def remove_v
    v = "aeiouAEIOU" #v = all vowels
    return "".join([char for char in text if char not in v]) 
#return the text(input) if the char not in v and join them together


main()

