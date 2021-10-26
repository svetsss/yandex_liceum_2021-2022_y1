a1 = float(input())
a2 = float(input())
b = str(input())
if (b == '*' or b == '/' or b == '+' or b == '-') and (a1 != 0 and a2 != 0):
    if b == '*':
        print(a1 * a2)
    elif b == '/':
        print(a1 / a2)
    elif b == '+':
        print(a1 + a2)
    elif b == '-':
        print(a1 - a2)
else:
    print('888888')