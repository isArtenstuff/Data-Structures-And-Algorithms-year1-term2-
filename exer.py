"""Exercise"""
scores = []
for _ in range(4):
    x = int(input())
    scores.append(x)
scores.sort(reverse=True)
my_score = sum(scores[:3])
print(my_score)
