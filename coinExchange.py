def convert_key(data):
    return {int(k): v for k, v in data.items()}

def main():
    import json
    amount = int(input())
    data = convert_key(json.loads(input()))
    coinExchange(amount, data)

def coinExchange(amount: int, coins: dict):
    hold = amount
    result = {10:0, 5:0, 2:0, 1:0}
    total_coins = 0
    for coin in sorted(coins.keys(), reverse=True):
        if hold <= 0:
            break
        use = min(hold // coin, coins[coin])
        if use > 0:
            result[coin] = use
            hold -= use * coin
            total_coins += use
    if hold != 0:
        print(f"Amount: {amount}")
        print("Coins are not enough.")
    else:
        print(f"Amount: {amount}")
        print("Coin exchange result:")
        for coin in sorted(result.keys(), reverse = True):
            print(f"  {coin} baht = {result[coin]} coins")
        print(f"Number of coins: {total_coins}")
main()