def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def average_of_primes(start, end):
    prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
    
    if not prime_numbers:
        return 0  # Avoid division by zero if there are no prime numbers
    
    return sum(prime_numbers) / len(prime_numbers)

# Finding average of prime numbers in the range (1, 10)
result = average_of_primes(1, 10)
print("Average of prime numbers in the range (1, 10):",result)