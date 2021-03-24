import math
limit = 104750


def init_list():
    lst = []
    for i in range(2, limit):
        lst.append(True)
    return lst


def sieve_erathostene():
    lst = init_list()
    primes_lst = []
    for i in range(2, int(math.sqrt(limit) + 1)):
        counter = 0
        if lst[i] == True:
            while True:
                if i**2 + (counter * i) >= len(lst):
                    break
                j = i**2 + counter * i
                lst[j] = False
                counter += 1
    for i in range(2, len(lst)):
        if lst[i] == True:
            primes_lst.append(i)
    return primes_lst


if __name__ == "__main__":
    print(sieve_erathostene()[-1])


