num = int(input("Enter a num: "))
a = 0
b = 1
print("Fibonacci series of",num,"numbers are: \n",a,b,end=" ")
for i in range(0,num-1):
    c = a + b
    a = b
    b = c
    print(c,end=" ")