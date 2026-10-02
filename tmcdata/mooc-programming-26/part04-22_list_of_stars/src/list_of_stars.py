# Write your solution here
def list_of_stars(numb):
    for i in numb:
        print('*' * i)

if __name__ == '__main__':
    num = [3,4,6,1,2]
    print(list_of_stars(num))