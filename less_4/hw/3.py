a = int(input())
b = 0
while a != 1:
    if a % 2 != 0:
        print('НЕТ')
        break
    a //= 2
    b += 1
else:
    print(b)