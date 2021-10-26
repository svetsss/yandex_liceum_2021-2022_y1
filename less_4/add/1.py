pas1 = input()
pas2 = input()
leght = len(pas1)
if leght >= 8:
    if '123' in pas1:
        print('Простой!')
    elif pas1 == pas2:
        print('OK')
    else:
        print('Различаются.')
else:
    print('Короткий!')