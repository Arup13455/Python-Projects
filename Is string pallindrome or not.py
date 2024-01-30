def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for a case-insensitive check
    clean_string = ''.join(input_string.split()).lower()
    reversed_string = clean_string[::-1]
    
    return clean_string == reversed_string

# Example usage:
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")