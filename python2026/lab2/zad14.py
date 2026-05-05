# Zadanie 14: utworz funkcje liczaca iloraz 3 parzystych liczb.
def quotient_three_even(a, b, c):
    if a % 2 != 0:
        return None
    if b % 2 != 0:
        return None
    if c % 2 != 0:
        return None
    if b == 0 or c == 0:
        return None

    result = a / b / c
    return result


a = int(input("Podaj pierwsza liczbe parzysta: "))
b = int(input("Podaj druga liczbe parzysta (nie 0): "))
c = int(input("Podaj trzecia liczbe parzysta (nie 0): "))

result = quotient_three_even(a, b, c)

if result is None:
    print("Blad: podaj 3 liczby parzyste, a b i c nie moga byc rowne 0.")
else:
    print("Iloraz =", result)
