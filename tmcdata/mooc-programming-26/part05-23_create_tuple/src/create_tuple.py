def create_tuple(x: int, y: int, z: int):
    first = min(x,y,z)
    middle = max(x,y,z)
    last = x+y+z

    return (first,middle,last)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))