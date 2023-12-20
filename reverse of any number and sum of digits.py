'''n = input("Enter any num: ")
print("reverse of",n,"is:",n[::-1])'''
n = int(input("Enter any num: "))
reverse = 0
sum = 0
while n != 0:
    remainder = n % 10
    sum += remainder
    reverse = reverse * 10 + remainder
    n //= 10

print("reverse is:",reverse)
print("sum is:",sum)
