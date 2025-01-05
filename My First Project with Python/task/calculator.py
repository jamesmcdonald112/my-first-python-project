# Write your code here
items_and_prices = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}

income = sum(items_and_prices.values())


print("Earned amount: ")
for item, price in items_and_prices.items():
    print(f"{item} : ${price}")
print()
print(f"Income: ${income}")
