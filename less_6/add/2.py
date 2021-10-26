a = int(input())
mean = int(input())
print(0)
for n in range(1, a):
    b = int(input())
    if b > mean:
        print('>')
    elif b < mean:
        print('<')
    else:
        print(0)
    mean = (mean * n + b) / (n + 1)