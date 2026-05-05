##### Zadanie 3
## Utworz funkcje z wieloma argumentami (x1,x2,...,xn),
## ktora przyjmuje z konsoli sekwencje liczb rozdzielonych przecinkami
## i zwraca: x1^x1, x2^x2, ..., xn^xn.
## Jesli liczba parametrow > 100, wypisz komunikat bledu.
## Nazwy parametrow: x1, x2, ..., xn.
## Uzyj docstringow (styl Google).


def powers_from_args(*args):
    """Liczy x^x."""
    if len(args) > 100:
        return 'Blad: za duzo parametrow (max 100).'
    return [x ** x for x in args]


def parse_csv_numbers(text):
    """Parsuje liczby CSV."""
    return [int(item.strip()) for item in text.split(',') if item.strip()]


user_data = '2,3,4,5'
numbers = parse_csv_numbers(user_data)
result = powers_from_args(*numbers)
print(result)
