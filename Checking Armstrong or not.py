'''num = int(input("Enter a num: "))
def check_Armstrong(n):
    sum = 0
    x = n
    while x != 0:
        r = x % 10
        sum += r**3
        x //= 10
    if n == sum:
        print(n,"is an armstrong num.")
    else:
        print(n,"is not an armstrong num.")

check_Armstrong(num)'''
num = int(input("Enter a num: "))
n = num
sum = 0
while n != 0 :
    r = n % 10
    sum += r**3
    n //= 10
if num == sum:
    print(num,"is an armstrong num.")
else:
    print(num,"is not an armstrong num.")