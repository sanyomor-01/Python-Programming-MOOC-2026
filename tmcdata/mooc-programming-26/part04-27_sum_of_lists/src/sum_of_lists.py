# Write your solution here"
def list_sum(a_list: list, b_list: list):
    acc = []
    for i in range(len(a_list)):
        s_sum = a_list[i] + b_list[i]
        acc.append(s_sum)
    return acc

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))