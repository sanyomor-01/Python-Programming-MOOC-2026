# Write your solution here
def everything_reversed(words):
    results = []
    for word in words[::-1]:
        results.append(word[::-1])
    return results
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)