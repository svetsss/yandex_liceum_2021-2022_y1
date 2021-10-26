a = int(input())
b = int(input())
c = int(input())
tmp = [a, b, c]
tmp.sort(reverse=True)
for t in tmp:
    print(t)