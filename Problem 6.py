import math

def square_difference(n):
    sum_square = 0
    square_sum = 0

    for i in range(1, n+1):
        sum_square += math.pow(i, 2)
        square_sum += i

    # Optimal solution: using arithmetic sum
    # f(n) = an^3 + bn^2 +cn + d -> f(0), f(1), f(2), f(3) -> solving
    # equation system

    return math.pow(square_sum, 2) - sum_square


if __name__ == "__main__":
    print(square_difference(100))
