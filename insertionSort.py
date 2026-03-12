import json
def insertion_sort(lst: list, last):
    lst = json.loads(lst)
    comparisons = 0
    current = 1
    while current <= last:
        hold = lst[current]
        walker = current - 1
        while walker >= 0:
            comparisons += 1
            if hold < lst[walker]:
                lst[walker + 1] = lst[walker]
                walker -= 1
            else:
                break
        lst[walker + 1] = hold        
        current += 1
        print(lst)
    print(f"Comparison times: {comparisons}")
insertion_sort(input(), int(input()))