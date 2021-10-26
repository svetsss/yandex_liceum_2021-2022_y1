text1 = input('Вы поступили в Яндекс Лицей?')
if text1 == 'да' or text1 == 'нет': 
    text2 = input('Вы чувствуете себя одиноко?')
    if text2 == 'да' or text2 == 'нет': 
        text3 = input('У вас есть проблемы с тревожностью?')
        if text3 == 'да' or text3 == 'нет': 
            text4 = input('У вас есть собака?')
            if text4 == 'да' or text4 == 'нет': 
                if text1 == text2 == text3 == text4:
                    print('Обратитесь к психиатру')
                elif text1 == text2 != text3 == text4:
                    print('Заведите друзей')
                elif text1 != text2 == text3 == text4:
                    print('Вы точно человек?')
                elif text1 != text2 != text3 == text4:
                    print('Вы обычный человек')
                elif text1 == text2 == text3 != text4:
                    print('Найдите себе занятие')
                elif text1 == text2 != text3 != text4:
                    print('Найдите себе занятие и друзей')
                elif text1 != text2 == text3 != text4:
                    print('Найдите собаку')
                elif text1 != text2 != text3 != text4:
                    print('Найдите кота')
                else:
                    print('Отвечайте только "да" или "нет"')                
            else:
                print('Отвечайте только "да" или "нет"')
        else:
            print('Отвечайте только "да" или "нет"')
    else:
        print('Отвечайте только "да" или "нет"')      
else:
    print('Отвечайте только "да" bли "нет"')      