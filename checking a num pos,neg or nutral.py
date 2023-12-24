# program to check if a num is positive,negative or zero
num = int(input("Enter a num: "))
if num > 0:
    print(f"{num} is  a positive num.")
elif num == 0:
    print("It is zero.")
else:
    print(f"{num} is a negative num.")
