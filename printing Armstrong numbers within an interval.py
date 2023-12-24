lower = int(input("Enter the lower limit here: "))
upper = int(input("Enter the upper limit here: "))
for num in range(lower, upper+1):
    order = len(str(num))
    sum = 0
    n = num

    while n != 0 :
       r = n % 10
       sum += r**order
       n //= 10
    
    if num == sum:
       print(num)
    