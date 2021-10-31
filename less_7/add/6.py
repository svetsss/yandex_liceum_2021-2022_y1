n = int(input())
f = -1
p = 0
for i in range(n):
    a = int(input())
    b = a % 256
    c = (a // 256) % 256
    d = a // 256 ** 2
    e = ((d + c + p) * 37) % 256
    if e != b or b >= 100:
        f = i
        break
    p = b
print(f)