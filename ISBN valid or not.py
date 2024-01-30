def is_valid_isbn_10(isbn):
    if len(isbn) != 10 or not isbn[:-1].isdigit():
        return False

    total = sum(int(digit) * (i + 1) for i, digit in enumerate(isbn[:-1]))
    check_digit = total % 11
    check_digit = 'X' if check_digit == 10 else str(check_digit)

    return check_digit == isbn[-1]

def is_valid_isbn_13(isbn):
    if len(isbn) != 13 or not isbn.isdigit():
        return False

    total = sum(int(digit) * (3 if i % 2 == 0 else 1) for i, digit in enumerate(isbn[:-1]))
    check_digit = (10 - (total % 10)) % 10

    return check_digit == int(isbn[-1])

# Get user input for ISBN
user_input_isbn = input("Enter an ISBN: ")

# Check ISBN validity
if len(user_input_isbn) == 10:
    print(f"Is ISBN-10 {user_input_isbn} valid? {is_valid_isbn_10(user_input_isbn)}")
elif len(user_input_isbn) == 13:
    print(f"Is ISBN-13 {user_input_isbn} valid? {is_valid_isbn_13(user_input_isbn)}")
else:
    print("Invalid ISBN length. Please enter a valid ISBN.")