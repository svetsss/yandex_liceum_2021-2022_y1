text1 = input()
text2 = input()
if text1 == 'да' and text2 == 'нет':
    print('ВЕРНО')
elif text1 == 'нет' and text2 == 'да':
    print('ВЕРНО')
elif text1 == 'нет' and text2 == 'нет':
    print('ВЕРНО')
elif text1 == 'да' and text2 == 'да':
    print('ВЕРНО')    
else:
    print('НЕВЕРНО')
    