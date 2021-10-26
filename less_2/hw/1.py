login = input()
adress = input()
if "@" in adress and '@' not in login:
    print('OK') 
elif ("@" not in adress and '@'not in login):
    print('Некорректный адрес')
elif ("@" in adress and '@' in login):
    print('Некорректный логин')
elif ('@' not in adress and '@' in login):
    print('Некорректный логин')