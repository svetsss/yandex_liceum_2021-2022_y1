x1 = 0
x2 = 1001
tf = False
while not tf:
    guessed = False
    number = (x1 + x2) // 2
    print(number)
    answer = input()
    if "<" not in answer and ">" not in answer and "=" not in answer:
        print("Неверный ввод")
    else:
        if answer == "<":
            x2 = number
        elif answer == ">":
            x1 = number
        elif answer == "=":
            tf = True