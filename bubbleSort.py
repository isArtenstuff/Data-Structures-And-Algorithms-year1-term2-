import json
def bubbleSort(lst, last):
    lst = json.loads(lst)
    current = 0
    sort = False
    comparison = 0
    while current <= last and sort == False:
        walker = last
        sort = True
        while walker > current:
            comparison += 1
            if lst[walker] < lst[walker -1]:
                sort = False
                hold = lst[walker]
                lst[walker] = lst[walker - 1]
                lst[walker - 1] = hold
            walker -= 1
        current += 1
        print(lst)
    print(f"Comparison times: {comparison}")
bubbleSort(input(), int(input()))