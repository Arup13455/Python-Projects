def analyze_string(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    digits = "0123456789"
    
    vowel_count = sum(1 for char in input_string if char in vowels)
    consonant_count = sum(1 for char in input_string if char in consonants)
    digit_count = sum(1 for char in input_string if char in digits)
    
    # Spaces are counted using the built-in count method
    space_count = input_string.count(' ')
    
    # Special characters are calculated as the difference between total characters and known characters
    special_char_count = len(input_string) - (vowel_count + consonant_count + digit_count + space_count)

    # Word count is calculated using split()
    word_count = len(input_string.split())

    return vowel_count, consonant_count, digit_count, space_count, special_char_count, word_count

# Example usage:
user_input = input("Enter a string: ")

vowels, consonants, digits, spaces, special_chars, words = analyze_string(user_input)

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special Characters: {special_chars}")
print(f"Word Count: {words}")