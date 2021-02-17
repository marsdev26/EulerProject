def mult(n):
    final_sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            final_sum += i
    return final_sum

if __name__ == "__main__":
    print(mult(1000))