from math import sqrt
dist = float(input())
speed = float(input())
i = 0
while dist - speed > 0.01:
    dist = sqrt((dist - speed) ** 2 + speed ** 2)
    i += 1
print(i)