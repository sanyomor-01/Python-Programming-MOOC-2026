def read_fruits():
    with open('fruits.csv') as file:
        fruits_and_price = {}

        for fruits in file:
            fruits = fruits.replace('\n', '')
            parts = fruits.split(';')
            fruit = parts[0]
            price = float(parts[1])

            fruits_and_price[fruit] = price

        return fruits_and_price

if __name__ == "__main__":
   print( read_fruits())