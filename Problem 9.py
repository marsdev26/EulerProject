
def check_3_possibilities_1000():
    for i in range(1, 999):
        for j in range(i+1, 999-i):
            if i + j + (1000 - i - j) == 1000 \
                    and (i**2 + j**2) == (1000 - i - j)**2:
                print(i*j*(1000 - i - j))

if __name__ == "__main__":
    check_3_possibilities_1000()