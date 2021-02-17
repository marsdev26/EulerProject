def palindromic_number_3_digits():
    curr_max = -1
    for i in range(100, 1000):
        for j in range(i, 1000):
            if (split(str(i*j)) == split(str(i*j))[::-1]) and (i*j > curr_max):
                curr_max = i*j
    return curr_max

def split(str):
    return [char for char in str]

if __name__ == "__main__":
    print(palindromic_number_3_digits())