n = int(input())
a = 0
p = 3.141592653589793
for i in range(1, n + 1):
    a += 1 / (i ** 2)
print((p ** 2) / a)