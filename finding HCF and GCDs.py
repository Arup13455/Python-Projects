# python program to find HCF and GCD between two numbers
a = int(input("Enter a's value: "))
b = int(input("Enter b's value: "))
def FindHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
print(f"The HCF of {a} and {b} is:",FindHCF(a,b))
if a > b:
    greater = a
else:
    greater = b
while(True):
    if greater % a == 0 and greater % b == 0:
        lcm = greater
        break
    greater += 1
print(f"The LCM of {a} and {b} is: {lcm}")

