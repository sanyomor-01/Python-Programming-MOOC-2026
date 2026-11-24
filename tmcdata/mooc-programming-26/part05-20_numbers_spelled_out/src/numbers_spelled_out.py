def dict_of_numbers():

    result = {}
    ones = {
        0: 'zero', 
        1: 'one', 
        2:'two', 
        3:'three', 
        4:'four', 
        5:'five', 
        6:'six', 
        7:'seven', 
        8:'eight', 
        9:'nine'
        }
    
    teens = {
        10: 'ten', 
        11:'eleven', 
        12:'twelve', 
        13:'thirteen', 
        14:'fourteen', 
        15:'fifteen', 
        16:'sixteen', 
        17:'seventeen', 
        18:'eighteen', 
        19:'nineteen'
        }
    
    compounds = {
        20:'twenty', 
        30:'thirty', 
        40:'forty', 
        50:'fifty', 
        60:'sixty', 
        70:'seventy', 
        80:'eighty', 
        90:'ninety'
        }


    for n in range(100):

        if n < 10:
            result[n] = ones[n]


        elif n < 20:
           result[n] = teens[n]
        
        elif n >= 20:
            tens_key = (n//10) * 10
            ones_key = n % 10
            if ones_key == 0:
                result[n] = compounds[tens_key]
            else:
                result[n] = compounds[tens_key] + '-' + ones[ones_key]

    return result


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
