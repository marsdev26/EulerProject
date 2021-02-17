def prime_factor(n):
    x = -1
    for i in range(2, int(n**(1/2))):
        while n % i == 0:
            n = n // i
            x = i
    return x
if __name__ == "__main__":
    print(prime_factor(600851475143))