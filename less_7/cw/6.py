sum = 0
a = int(input())
count = 0
while a != 0:
    sum += a
    if sum == 10:
        count += 1
        print(count)
        break
    count += 1
    a = int(input())