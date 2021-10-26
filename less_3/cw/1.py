a = input()
b = input()
if a == "Тула" and b != "Пенза" and a != b or b == "Пенза" and a != "Тула" and a != b:
    print("ДА")
else:
    print("НЕТ")
