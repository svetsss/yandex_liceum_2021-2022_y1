count = int(input())
nmax = int((2 * count) ** (1 / 2))
for i in range(nmax, 0, -1):
    if (2 * count - i * i + i) % (2 * i) == 0:
        print((2 * count - i * i + i) // (2 * i))
        break