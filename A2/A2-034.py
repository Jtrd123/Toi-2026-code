import math

def is_prime(num) :
    if num <= 1 :
        return False
    
    limit = int(math.sqrt(num))
    for i in range(2, limit + 1) :
        if num % i == 0 :
            return False
    
    return True

n = int(input())

if is_prime(n) :
    print("Yes")

    primes = []
    for i in range(2, n + 1) :
        if is_prime(i) :
            primes.append(i)

    print(*primes)
else :
    print("No")