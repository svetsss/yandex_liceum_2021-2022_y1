p1 = int(input())
p2 = int(input())
reserve = False
while p2 != 0:
    if not reserve:
        if p1 < p2:
            min = p2
            reserve = True
    else:
        if p1 > p2:
            max = p2
            break
    p1 = p2
    p2 = int(input())
print(min, max, max - min)

