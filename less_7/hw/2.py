x = 0
y = 0
n = 0
flag = True
cl_x = int(input())
cl_y = int(input())
stor = input()
kol = int(input())
while stor != 'стоп':
    if cl_x == x and cl_y == y:
        flag = False
    if stor == 'север':
        y += kol
        if flag:
            n += 1
    elif stor == 'запад':
        x -= kol
        if flag:
            n += 1
    elif stor == 'юг':
        y -= kol
        if flag:
            n += 1
    elif stor == 'восток':
        x += kol
        if flag:
            n += 1
    stor = input()
    if stor != 'стоп':
        kol = int(input())
print(n)