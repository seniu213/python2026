# Zadanie 8: wczytaj a, b, c i oblicz pierwiastki rownania kwadratowego ax^2 + bx + c = 0.
import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    if b == 0:
        print("To nie jest rownanie (a=0 i b=0).")
    else:
        x = -c / b
        print("Rownanie liniowe, jedno rozwiazanie: x =", x)
else:
    delta = b * b - 4 * a * c

    if delta > 0:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b - sqrt_delta) / (2 * a)
        x2 = (-b + sqrt_delta) / (2 * a)
        print("Dwa pierwiastki rzeczywiste: x1 =", x1, ", x2 =", x2)
    elif delta == 0:
        x = -b / (2 * a)
        print("Jeden pierwiastek podwojny: x =", x)
    else:
        sqrt_delta = math.sqrt(-delta)
        real_part = -b / (2 * a)
        imag_part = sqrt_delta / (2 * a)

        x1_text = str(real_part) + " - " + str(imag_part) + "i"
        x2_text = str(real_part) + " + " + str(imag_part) + "i"

        print("Pierwiastki zespolone:")
        print("x1 =", x1_text)
        print("x2 =", x2_text)
