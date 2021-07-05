def reversed(string):
    x = string.split()  # Split string to list
    i = 1
    y = []
    for _ in x:
        y.append(x[len(x)-i])  # Add elements from X list to the end of Y list but in reversed order
        i += 1
    return " ".join(y)  # Join all elements of list Y to create string


strU = input("Give me long string with white spaces: ")
print(reversed(strU))
