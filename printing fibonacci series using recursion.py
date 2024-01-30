a = 0
n = int(input(("Enter a pos int num: ")))
print("Fibonacci series: ")
def get_fibonacci(x):
	if x == 0 :
		return 0
	elif x == 1:
		return 1
	else:
		return (get_fibonacci(x-1)+get_fibonacci(x-2))
	
for i in range(n):
	print(get_fibonacci(a))
	a += 1
