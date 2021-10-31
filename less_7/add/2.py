a = False
n = int(input())
for i in range(n):
    text = input()
    if ('Пёс' in text) or ('пёс' in text):
        a = False
    elif ('Кот' in text) or ('кот' in text):
        a = True
if a:
    print('МЯУ')
else:
    print('НЕТ')
