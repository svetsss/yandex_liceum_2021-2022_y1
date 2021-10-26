x = int(input())
i = 1
w = x + (x - 1)
for i in range(1, x + 1):
    print("{0:^{1}.{2}}".format("*" * (i + (i - 1)), w, w))