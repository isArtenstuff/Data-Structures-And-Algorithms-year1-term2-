import json
def selectionSort(lst, last):
    lst = json.loads(lst)
    current = 0
    comparisons = 0
    while current < last:
        smallest = current
        walker = current + 1
        while walker <= last:
            comparisons += 1
            if lst[walker] < lst[smallest]:
                smallest = walker
            walker += 1
        hold = lst[smallest]
        lst[smallest] = lst[current] 
        lst[current] = hold
        current += 1
        print(lst)
    print(f"Comparison times: {comparisons}")
selectionSort(input(), int(input()))