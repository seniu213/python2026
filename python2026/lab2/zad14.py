# Zadanie 14: utworz funkcje liczaca iloraz 3 parzystych liczb, uzywajac one line statement.
def quotient_three_even(a, b, c):
    return a / b / c if all(n % 2 == 0 for n in (a, b, c)) and b != 0 and c != 0 else None


a = int(input("Podaj pierwsza liczbe parzysta: "))
b = int(input("Podaj druga liczbe parzysta (nie 0): "))
c = int(input("Podaj trzecia liczbe parzysta (nie 0): "))

result = quotient_three_even(a, b, c)

if result is None:
    print("Blad: podaj 3 liczby parzyste, a b i c nie moga byc rowne 0.")
else:
    print(f"Iloraz = {result}")

