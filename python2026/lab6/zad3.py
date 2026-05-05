import math
import os


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
INPUT_PATH = os.path.join(DATA_DIR, "zad3_input.txt")


def licz(fun):
    try:
        tekst = fun.replace(" ", "")
        if "x^2" not in tekst:
            raise ValueError("To nie jest rownanie kwadratowe.")

        tekst = tekst.replace("-", "+-")
        if tekst.startswith("+-"):
            tekst = "-" + tekst[2:]

        a = 0.0
        b = 0.0
        c = 0.0

        for czesc in tekst.split("+"):
            if not czesc:
                continue

            if "x^2" in czesc:
                k = czesc.replace("x^2", "")
                if k in ("", "+"):
                    a = 1.0
                elif k == "-":
                    a = -1.0
                else:
                    a = float(k)
            elif "x" in czesc:
                k = czesc.replace("x", "")
                if k in ("", "+"):
                    b = 1.0
                elif k == "-":
                    b = -1.0
                else:
                    b = float(k)
            else:
                c = float(czesc)

        if a == 0:
            raise ValueError("a nie moze byc 0.")

        delta = b * b - 4 * a * c
        if delta < 0:
            raise ValueError("Brak pierwiastkow rzeczywistych.")

        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2

    except Exception as e:
        print("Blad:", e)
        return None


assert set(licz("x^2+4x-21")) == {3.0, -7.0}

try:
    if not os.path.exists(INPUT_PATH):
        with open(INPUT_PATH, "w", encoding="utf-8") as f:
            f.write("x^2+4x-21")

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        rownanie = f.read().strip()

    wynik = licz(rownanie)
    print("Rownanie z data/zad3_input.txt:", rownanie)
    print("Pierwiastki:", wynik)
except Exception as e:
    print("Blad:", e)
