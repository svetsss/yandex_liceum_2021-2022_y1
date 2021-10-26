pas1 = input()
pas2 = input()
leght = len(pas1)
if leght >= 8:
    if pas1 == pas2:
        print('OK')
    else:
        print('Различаются.')
else:
    print('Короткий!')
