kolchisel = 0
a = int(input())
if a == 1:
    print(a)
    print('НЕТ')
else:
    for i in range(1, a + 1):
        if a % i == 0:
            kolchisel = kolchisel + 1
            print(i, end=" ")
    print()
    if kolchisel > 2:
        print("НЕТ")
    else:
        print("ПРОСТОЕ")