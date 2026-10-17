def factorials(n: int):
    my_dict = {}
    ans = 1

    for i in range(1, n+1):
        ans *= i
        my_dict[i] = ans
        
    return my_dict

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])