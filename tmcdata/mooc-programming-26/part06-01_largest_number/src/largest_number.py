def largest():
    with open('numbers.txt') as num_file:
        largest = 0
        
        for number in num_file:
            number = number.replace('\n', '')
            if int(number) > largest:
                largest = int(number)

        
        return largest


if __name__ == '__main__':
    largest()


