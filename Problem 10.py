import math

def is_prime(n):

    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def sum_prime(n):
    primes = []
    for i in range(2,n):
        if is_prime(i):
            primes.append(i)
    return sum(primes)

if __name__ == "__main__":
    print(sum_prime(2000000))