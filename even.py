"""Even"""
def is_even(k):
    return (k & 1) == 0
n = int(input())
print(is_even(n))
