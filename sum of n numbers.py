'''n = int(input("enter number: "))
sum = n * (n + 1) / 2
print("sum of",n,"numbers is:", sum)'''
n = int(input("enter number: "))
sum = 0
for n in range(1,n+1):
    sum += n
print("sum of",n,"numbers is:", sum)



