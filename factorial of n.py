# python program to find the factorial of a number provided by user
# to take input from user
num = int(input("enter a number: "))
factorial = 1
# checking the number is negative, positive or zero
if num < 0:
    print("sorry! factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print("The factorial of", num, "is", float(factorial))








