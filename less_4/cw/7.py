astronauts = 0
shortest = 190
tallest = 0
kandidat = input()
while kandidat != "!":
    if (int(kandidat) <= 190) and (int(kandidat) >= 150):
        astronauts = astronauts + 1
        if int(kandidat) < shortest:
            shortest = int(kandidat)
        if int(kandidat) > tallest:
            tallest = int(kandidat)
    kandidat = input()
print(astronauts)
print(shortest, tallest)