cat_in_phrase = False
count = 0
phrase = ''
kot = 0
while phrase != 'СТОП':
    phrase = input()
    count += 1
    if ('Кот' in phrase) or ('кот' in phrase):
        kot += 1
    if not(cat_in_phrase):
        if ('Кот' in phrase) or ('кот' in phrase):
            cat_in_phrase = True
            number = count
if cat_in_phrase:
    print(kot, number)
else:
    print(0, -1)