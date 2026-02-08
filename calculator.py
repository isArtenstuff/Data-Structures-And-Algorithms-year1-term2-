def calculator():
    output = 0
    n = int(input())
    for i in range(1, n + 1):
        if n == 1:
            output = 1
        else:
            output += len(str(i)) + 1
    return output
print(calculator())