##### Zadanie 2
## Napisz funkcje, ktora znajdzie liczby podzielne przez 7,
## ale niebedace wielokrotnoscia 5, w zakresie od x do y (wlacznie).
## Wynik wypisz jako sekwencje rozdzielona przecinkami.
## Uzyj docstringow (styl Google).
## Dla Lab6: obsluz wyjatki.
## Zapisz wynik do pliku *.pkl (modul pickle).

import pickle


def find_numbers_safe(x, y):
    """Zwraca liczby po walidacji."""
    try:
        x = int(x)
        y = int(y)
    except ValueError as err:
        raise ValueError('x i y musza byc int') from err

    if x > y:
        raise ValueError('x musi byc <= y')

    return [n for n in range(x, y + 1) if n % 7 == 0 and n % 5 != 0]


try:
    x = 1000
    y = 2101
    result = find_numbers_safe(x, y)

    with open('zad2_result.pkl', 'wb') as file:
        pickle.dump(result, file)

    print(','.join(map(str, result)))
    print('Zapisano: zad2_result.pkl')
except Exception as error:
    print('Blad:', error)
