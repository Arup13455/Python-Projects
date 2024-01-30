# Get user input for the string
user_input = input("Enter a string: ")

# Initialize an empty dictionary to store character frequencies
char_frequency = {}

# Count the frequency of each character
for char in user_input:
    char_frequency[char] = char_frequency.get(char, 0) + 1

# Display the character frequencies in ascending order
print("Character frequencies in ascending order:")
for char in sorted(char_frequency):
    print(f"{char}: {char_frequency[char]}")