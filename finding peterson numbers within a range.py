lower = int(input("Enter the lower limit here: "))
upper = int(input("Enter the upper limit here: "))
for num in range(lower, upper+1):
    def get_fact(a):
        return 1 if a == 0 or a == 1 else a*get_fact(a-1)

    def check_peterson(x):
        y = x
        sum = 0
        while x != 0:
           r = x % 10
           sum += get_fact(r)
           x //= 10
        if sum == y:
            print(f"{y}")

    check_peterson(num)