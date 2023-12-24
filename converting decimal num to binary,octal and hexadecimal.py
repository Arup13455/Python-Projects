# python program to convert Decimal num to Bionary,octal and Hexadecimal num
# Decimal num 0 to 9 and it's base 10
# Binary num 0 and 1 and it's base 2,prefix 0b
# for decimal base 8 and hexadecimal 16,prefix 0o and 0x
num = int(input("Enter a num: "))
print(f"The conversion of decimal num {num} are: ")
print(f"{bin(num)} in binary")
print(f"{oct(num)} in octal")
print(f"{hex(num)} in hexadecimal")
