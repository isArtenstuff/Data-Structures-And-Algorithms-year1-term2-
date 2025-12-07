"""Max Min Avg"""
import json
def result(scores_list):
    MAXIMUM = scores_list[0]
    MINIMUM = scores_list[0]
    total = 0

    for x in scores_list:
        if x > MAXIMUM:
            MAXIMUM = x
        if x < MINIMUM:
            MINIMUM = x
        total += x
    
    average = total / len(scores_list)
    
    return (round(MAXIMUM, 2), round(MINIMUM, 2), round(average, 2))

data = json.loads(input())
print(result(data))
