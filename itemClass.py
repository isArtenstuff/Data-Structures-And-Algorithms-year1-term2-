class Item:
    def __init__(self, name: str, price: int, weight: float):
        self.name = name
        self.price = price
        self.weight = weight
    
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_weight(self):
        return self.weight

def knapsack(itemList, amount):
    items = sorted(itemList, key = lambda x:x.price/x.weight, reverse=True)
    total_price = 0
    current_weight = 0
    selected = []
    for item in items:
        if current_weight + item.weight <= amount:
            selected.append(item)
            current_weight += item.weight
            total_price += item.price
    
    print(f"Knapsack Size: {amount} kg")
    print("===============================")
    for i in selected:
        print(f"{i.name} -> {i.weight} kg -> {i.price} THB")
    print(f"Total: {total_price} THB")

def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()