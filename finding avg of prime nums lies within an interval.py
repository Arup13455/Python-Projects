num = int(input("Enter a num for taking range: "))
sum = 0
count = 0
for i in range(1,num+1):
    c = 0
    for j in range(2,int(i/2+1)):
        if i % j == 0:
            c += 1
            break
    if c == 0 and i != 1:
        sum += i
        count += 1
        avg = sum / count
        
print(f"The avg of prime numbers between (1-{num}): {avg}")

        