import sys

if len(sys.argv) != 2:
    print("Usage: python script.py price1 price2 price3")
    sys.exit(1)

    prices = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]

min_price = min(prices)
max_price = max(prices)
avg_price = sum(prices) / len(prices)

print(f"Minimum Price: {min_price}")
print(f"Maximum Price: {max_price}")
print(f"Average Price: {avg_price:.2f}")