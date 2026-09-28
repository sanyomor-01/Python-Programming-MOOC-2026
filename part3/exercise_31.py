# Print many times

def print_many_times(text, times):
    while times > 0:
        print(text)
        times -= 1

# Testing the function
if __name__ == '__main__':
    print_many_times('Programming', 3)