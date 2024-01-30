# write a python program to find the factorial of first 10 prime numbers
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
        num += 1
    return primes

# Calculate factorial of the first 10 prime numbers
primes = first_n_primes(10)
factorials = [factorial(p) for p in primes]

# Print the results
for prime, factorial_value in zip(primes, factorials):
    print(f"Factorial of {prime}: {factorial_value}")