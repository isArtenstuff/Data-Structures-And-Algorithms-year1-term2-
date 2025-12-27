"""Quiz 1"""
"""input 12, 25
    ouput 12, 14, 16, 18, 20, 22, 24,
"""
first  = int(input())
maxx = int(input())
def print_asc(n, max):
    if n > max:
        return
    else:
        print(n, end=", ")
        n += 2
        print_asc(n, max)
print_asc(first, maxx)
