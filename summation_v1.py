def summationv1(n):
    output = 0
    for i in range(n, 0, -1):
        output += i
    print(output)
summationv1(int(input()))