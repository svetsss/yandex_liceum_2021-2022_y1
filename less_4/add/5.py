while True:
    pas1 = input()
    pas2 = input()
    a = True
    if len(pas1) < 8:
        a = False
        print("Короткий!")
    elif "123" in pas1:
        a = False
        print("Простой!")
    elif pas1 != pas2:
        a = False
        print("Различаются.")
    elif a:
        break
print("OK")