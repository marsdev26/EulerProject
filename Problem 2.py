def even_fib(n):
    arr_fib = []
    arr_fib.append(0)
    arr_fib.append(1)
    final_sum = 0
    for i in range(2, n):
        arr_fib.append(arr_fib[i - 1] + arr_fib[i - 2])
        elem = arr_fib[i-1] + arr_fib[i-2]
        if elem > 4000000:
            return final_sum
        if elem % 2 == 0:
            final_sum += elem

    return final_sum



if __name__ == "__main__":
    print(even_fib(4000000))