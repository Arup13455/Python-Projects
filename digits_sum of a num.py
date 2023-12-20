# sum of digits of any num
num = int(input("Enter a num: "))
n = num
sum = 0
while n != 0 :
    r = n % 10
    sum += r
    n //= 10

print("sum of digits of",num,"are",sum)

