'''# swaping two varibles with using third variable
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = a
a = b
b = c
print(f"After swapping {b} and {a} are: ",a,b)
'''
# swaping two variables without using third variable
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
a += b
b = a-b
a -= b
print(f"After swapping {b} and {a} are: ",a,b)