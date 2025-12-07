"""Recursive GCD"""
def recursiveGCD(a, b):
    if b == 0:
        return a
    else:
        return recursiveGCD(b, a % b)
    
n1 = int(input())
n2 = int(input())

print(recursiveGCD(n1, n2))
