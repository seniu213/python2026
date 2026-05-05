##### Zadanie 4
## Utworz funkcje z wieloma argumentami (x1,x2,...,xn),
## ktora przyjmuje z konsoli sekwencje liczb rozdzielonych przecinkami
## i zwraca: x1^x1, x2^x2, ..., xn^xn.
## Jesli liczba parametrow > 100, wypisz komunikat bledu.
## Uzyj dynamicznych nazw zmiennych: exec() lub globals() lub locals().
## Nazwy parametrow: x1, x2, ..., xn.
## Uzyj docstringow (styl Google).
## Dla Lab6: obsluz wyjatki.


def dynamic_powers(csv_values):
    """Tworzy x1..xn i liczy potegi."""
    try:
        numbers = [int(item.strip()) for item in csv_values.split(',') if item.strip()]
    except ValueError:
        return 'Blad: podaj tylko int.'

    if len(numbers) > 100:
        return 'Blad: za duzo parametrow (max 100).'

    if not numbers:
        return []

    scope = {}
    result = []

    for i, value in enumerate(numbers, start=1):
        exec(f'x{i} = {value}', {}, scope)
        xi = scope[f'x{i}']
        result.append(xi ** xi)

    return result


try:
    user_data = '1,2,3,4'
    print(dynamic_powers(user_data))
except Exception as error:
    print('Blad:', error)
