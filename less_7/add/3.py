n = int(input())
for i in range(n):
    count = 0
    while True:
        a = input()
        if a == 'раз':
            count += 1
            a = input()
            if a == 'два':
                count += 1
                a = input()
                if a == 'три':
                    count += 1
                    a = input()
                    if a == 'четыре':
                        count += 1
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break
    print('Правильных отсчётов было ', count, ', но теперь вы ошиблись.', sep='')
print('На сегодня хватит.')