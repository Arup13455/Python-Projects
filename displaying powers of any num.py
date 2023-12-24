# python program to display powers of any number using anonymous function.
# anonymous function = lambda
num = int(input("Enter a num: "))
nterms = int(input("Enter number of terms here: "))
result = list(map(lambda x : num ** x, range(nterms+1)))
print(result)
for i in range(nterms+1):
    print(f"The value of {num} raised to power {i} is {result[i]}")