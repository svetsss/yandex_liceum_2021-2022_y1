import math
while True:
    a = int(input())
    zn = input()
    if zn == 'x':
        print(a)
        exit()
    elif zn == '+':
        b = int(input())
        print(a + b)
    elif zn == '-':
        b = int(input())
        print(a - b)
    elif zn == '*':
        b = int(input())
        print(a * b)
    elif zn == '/':
        b = int(input())
        if b != 0:
            print(a // b)
    elif zn == '%':
        b = int(input())
        if b != 0:
            print(a % b)
    elif zn == '!':
        if a >= 0:
            print(math.factorial(a))