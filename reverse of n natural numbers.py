n = int(input("Enter any number: "))
print(f"List of natural numbers from {n} to 1 in reverse order: ")
while n > 0:
    n -= 1
    print(n+1,"\n",end = ' ')
    