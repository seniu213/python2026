import stars


rozmiar = int(input('Podaj rozmiar liter: '))

print('Litera E:')
stars.Poziom(rozmiar)
for _ in range(rozmiar - 2):
    stars.Pion(1)
stars.Poziom(rozmiar)
for _ in range(rozmiar - 2):
    stars.Pion(1)
stars.Poziom(rozmiar)

print('Litera L:')
for _ in range(2 * rozmiar - 1):
    stars.Pion(1)
stars.Poziom(rozmiar)
