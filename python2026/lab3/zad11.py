Poziom = lambda ile: print('*' * ile)
Pion = lambda ile: list(map(lambda _: print('*'), range(ile)))


litera = input('Podaj litere E albo L: ').upper()
rozmiar = int(input('Podaj rozmiar litery: '))

if litera == 'E':
    Poziom(rozmiar)
    Pion(rozmiar - 2)
    Poziom(rozmiar)
    Pion(rozmiar - 2)
    Poziom(rozmiar)
elif litera == 'L':
    Pion(2 * rozmiar - 1)
    Poziom(rozmiar)
else:
    print('Podano inna litere')
