a = 1
for i in range(6):
    n = int(input())
    if n != 0:
        a *= n
    else:
        a *= 1
print(a)