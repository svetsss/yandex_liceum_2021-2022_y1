amount = int(input())
b = 1
total = 0
num = amount
a = 0
while num != 0:
    n = int(input())
    a += 1
    while a % 2 == 0:
        total -= n
        break
    while a % 2 != 0:
        total += n
        break
    num -= 1
print(total)