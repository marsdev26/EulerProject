def evenly_divisible():
    starting_point = 22

    while True:
        if (checking(starting_point)):
            return starting_point
        else:
            starting_point += 1


def checking(n):  # 20, 19, 18, 17, 16, 15, 14,13, 12,11 10, 9, 8, 7, 6, 5,
    # 4, 3, 2
    if n % 20 == 0 and n % 18 == 0 and n % 19 == 0 and n % 17 == 0 and n % 16 == 0 \
            and n % 14 == 0 and n % 13 == 0 and n % 15 == 0 and n % 11 == 0 and n % 12 == 0:
        return True
    return False


if __name__ == "__main__":
    print(evenly_divisible())
