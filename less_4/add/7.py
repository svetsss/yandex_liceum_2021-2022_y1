minimum = 0
x = int(input())
y = int(input())
x1 = 0
y1 = 0
move = 'север'
movement = input()
while movement != 'стоп':
    if int(x) == x1 and int(y) == y1:
        print(minimum)
        print(move)
        break
    else:
        minimum += 1
        if movement == 'вперёд':
            steps = int(input())
            if move == 'север':
                y1 += steps
            elif move == 'запад':
                x1 -= steps
            elif move == 'юг':
                y1 -= steps
            elif move == 'восток':
                x1 += steps
        elif movement == 'направо':
            if move == 'север':
                move = 'восток'
            elif move == 'восток':
                move = 'юг'
            elif move == 'юг':
                move = 'запад'
            elif move == 'запад':
                move = 'север'
        elif movement == 'налево':
            if move == 'север':
                move = 'запад'
            elif move == 'запад':
                move = 'юг'
            elif move == 'юг':
                move = 'восток'
            elif move == 'восток':
                move = 'север'
        elif movement == 'разворот':
            if move == 'север':
                move = 'юг'
            elif move == 'юг':
                move = 'север'
            elif move == 'запад':
                move = 'восток'
            elif move == 'восток':
                move = 'запад'
        if int(x) == x1 and int(y) == y1:
            print(minimum)
            print(move)
            break
        movement = input()
else:
    if x == 0 and y == 0:
        print(0)
        print("север")