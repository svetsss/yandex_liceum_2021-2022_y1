a = int(input())
b = False
for i in range(a):
    c = input()
    if ('Кот' in c) or ('кот' in c):
        b = True
        break
if b:
    print('МЯУ')
else:
    print('НЕТ')