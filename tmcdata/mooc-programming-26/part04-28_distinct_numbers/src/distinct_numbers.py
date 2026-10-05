# Write your solution here
def distinct_numbers(numbers):
    if not numbers:
        return []
    
    s_numbs = sorted(numbers)
    n_list = [s_numbs[0]]

    for num in s_numbs:
        if num != n_list[-1]:
            n_list.append(num)
            
    return n_list

if __name__ == '__main__':
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))