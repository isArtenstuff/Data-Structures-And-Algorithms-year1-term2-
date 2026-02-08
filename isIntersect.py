import ast

def isIntersect(a, b, c):
    return len(set(a) & set(b) & set(c)) > 0

a = ast.literal_eval(input())
b = ast.literal_eval(input())
c = ast.literal_eval(input())

print(isIntersect(a, b, c))
