e = True
o = False
num = int(input())
for i in range(num):
    w = input()
    if w == 'С кем война?':
        if e:
            print('Евразия')
        else:
            print('Остазия')
    elif w == 'С кем мир?':
        if not o:
            print('Остазия')
        else:
            print('Евразия')
    else:
        e, o = o, e
