n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
d1 = min(a, b, c, d)
d4 = max(a, b, c, d)
d2 = 0
d3 = 0
if a == d1:
    d2 = min(b, c, d)
    if b == d2:
        d3 = min(c, d)
    elif c == d2:
        d3 = min(c, b)
    elif d == d2:
        d3 = min(b, c)
elif b == d1:
    d2 = min(a, c, d)
    if a == d2:
        d3 = min(c, d)
    elif c == d2:
        d3 = min(d, a)
    elif d == d2:
        d3 = min(a, c)
elif c == d1:
    d2 = min(b, a, d)
    if a == d2:
        d3 = min(b, d)
    elif b == d2:
        d3 = min(d, a)
    elif d == d2:
        d3 = min(a, b)
elif d == d1:
    d2 = min(a, c, b)
    if a == d2:
        d3 = min(c, b)
    elif c == d2:
        d3 = min(b, a)
    elif b == d2:
        d3 = min(a, c)
if d1 == 0 and d2 != 0 and d3 != 0 and d4 != 0:
    print(f"{d2}{d1}{d3}{d4}")
elif d2 == 0 and d1 != 0 and d3 != 0 and d4 != 0:
    print(f"{d1}{d2}{d3}{d4}")
elif d3 == 0 and d2 != 0 and d3 != 0 and d4 != 0:
    print(f"{d1}{d3}{d2}{d4}")

elif d1 == 0 and d2 == 0 and d3 != 0 and d4 != 0:
    print(f"{d3}{d1}{d2}{d4}")
elif d2 == 0 and d3 == 0 and d1 != 0 and d4 != 0:
    print(f"{d1}{d2}{d3}{d4}")
elif d3 == 0 and d4 == 0 and d2 != 0 and d1 != 0:
    print(f"{d1}{d3}{d4}{d2}")
elif d1 == 0 and d4 == 0 and d2 != 0 and d3 != 0:
    print(f"{d2}{d1}{d4}{d3}")

elif d1 == 0 and d2 == 0 and d3 == 0 and d4 != 0:
    print(f"{d4}{d1}{d2}{d3}")
elif d2 == 0 and d1 == 0 and d4 == 0 and d3 != 0:
    print(f"{d3}{d2}{d1}{d4}")
elif d1 == 0 and d4 == 0 and d3 != 0 and d2 != 0:
    print(f"{d2}{d3}{d4}{d1}")
elif d2 == 0 and d4 == 0 and d3 != 0 and d1 != 0:
    print(f"{d1}{d3}{d4}{d2}")

elif d1 != 0 and d2 != 0 and d3 != 0 and d4 != 0:
    print(f"{d1}{d2}{d3}{d4}")
