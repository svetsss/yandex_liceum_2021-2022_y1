price = float(input())
total = 0
while price >= 0:
    if price > 1000:
        price = price - price * 0.05
    total = total + price
    price = float(input())
print(total)