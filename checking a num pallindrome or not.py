#checking a num pallindrome or not
x = int(input("Enter a num: "))
n = x
reverse = 0
while n != 0:
    r = n % 10
    reverse = reverse*10 + r
    n //= 10

if x == reverse:
    print(x,"is pallindrome")
else:
    print(x,"is not pallindrome")