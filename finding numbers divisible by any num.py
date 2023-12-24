# finding numbers divisible by any num (user given) within an interval
'''num = int(input("Enter a num: "))
a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))
print(f"The numbers divisible by {num} are: ")
for i in range(a,b+1):
    if i % num == 0:
        print(i)'''
num = int(input("Enter a num: "))
a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))
result = list(filter(lambda x: x % num == 0, range(a,b+1)))
print(f"The numbers divisible by {num} are: {result}")