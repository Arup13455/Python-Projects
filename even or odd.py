# to check numbers even or odd
""" x = int(input("enter number:"))
if x % 2 == 0:
    print(x, "is even number")
else:
    print(x, "is odd number")"""
'''def main():
    x = int(input("enter number:"))
    is_even(x)

def is_even(n):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
main()'''


def main():
    x = int(input("enter number:"))
    if is_even(x):
        print(x, "is even")
    else:
        print(x, "is odd")


def is_even(n):
    return n % 2 == 0


main()
'''return True if n % 2 == 0 else False
main()'''
''' if n % 2 == 0:
        return True
    else:
        return False
main()'''
