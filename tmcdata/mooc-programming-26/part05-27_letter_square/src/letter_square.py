layers = int(input("layers: "))
size = layers * 2 -1 # size of the square to print
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for row in range(size):
    for col in range(size):
        top = row 
        left = col
        distance_from_bottom = size - row -1
        distance_from_left = size - col -1
        distance = min(top,left, distance_from_left, distance_from_bottom)# to know the smallest distance from the edge of the square.

        #map the distance to a letter
        # distance = 0 => "C" ==>  letters[layers- distance -1]
        # distance = 1 => "B"
        # distance = 2 => "A"
        
        print(f"{letters[layers- distance -1]}", end='')
    print()

