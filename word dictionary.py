# Have a python dictionary that has a key/value pair that represent a word with definition
# Collect input from the user, input is a word
# Check if the word is in the dictionary
# print the definition
def main():
    word_dictionary = {
        'Hi': "A way of greeting",
        'Eyes': "An organ for seeing",
        'Earth': "A planet in space",
    }
    while True:
        word = input("Enter a word:")
        if word == "":
            print("Enter again")
            continue
        elif word in word_dictionary:
            print(word, ":", word_dictionary[word])
        else:
            print("Invalid word")


main()
