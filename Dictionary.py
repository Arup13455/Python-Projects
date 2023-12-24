from PyDictionary import PyDictionary
a = input("Enter the word you want to get the meaning: ")

dictionary = PyDictionary(a)


print(dictionary.getMeanings())

