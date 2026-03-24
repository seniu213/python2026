# Zadanie 8: wczytaj a, b, c i oblicz pierwiastki rownania kwadratowego ax^2 + bx + c = 0.
import cmath

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    if b == 0:
        print("To nie jest rownanie (a=0 i b=0).")
    else:
        x = -c / b
        print(f"Rownanie liniowe, jedno rozwiazanie: x = {x}")
else:
    delta = b**2 - 4 * a * c
    sqrt_delta = cmath.sqrt(delta)
    x1 = (-b - sqrt_delta) / (2 * a)
    x2 = (-b + sqrt_delta) / (2 * a)

    if delta > 0:
        print(f"Dwa pierwiastki rzeczywiste: x1 = {x1.real}, x2 = {x2.real}")
    elif delta == 0:
        print(f"Jeden pierwiastek podwojny: x = {x1.real}")
    else:
        print(f"Pierwiastki zespolone: x1 = {x1}, x2 = {x2}")

