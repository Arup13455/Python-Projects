# program to find  the largest among 3 numbers
a = int(input('Enter the value in a: '))
b = int(input('Enter the value in b: '))
c = int(input('Enter the value in c: '))
if a > b and a > c:
    print(f"{a} is largest.")
elif b > c:
    print(f"{b} is largest.")
else:
    print(f"{c} is largest.")