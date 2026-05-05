import csv
import math
import os


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CSV_PATH = os.path.join(DATA_DIR, "titanic_train.csv")


def dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Blad: dzielenie przez zero.")
    except TypeError:
        print("Blad: podaj liczby.")


def pierwiastek(x):
    try:
        if x < 0:
            raise ValueError
        return math.sqrt(x)
    except ValueError:
        print("Blad: pierwiastek z liczby ujemnej.")
    except TypeError:
        print("Blad: podaj liczbe.")


def pobierz_liczby_z_data(path_csv):
    with open(path_csv, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fare = row.get("Fare", "").strip()
            pclass = row.get("Pclass", "").strip()
            if fare and pclass:
                return float(fare), float(pclass)
    raise ValueError("Brak danych liczbowych w pliku.")


assert dzielenie(10, 2) == 5
assert pierwiastek(9) == 3

try:
    fare, pclass = pobierz_liczby_z_data(CSV_PATH)
    print("Dane z data/titanic_train.csv: Fare =", fare, "Pclass =", pclass)
    print("Fare / Pclass =", dzielenie(fare, pclass))
    print("sqrt(Fare) =", pierwiastek(fare))
except FileNotFoundError:
    print("Blad: nie znaleziono data/titanic_train.csv")
except Exception as e:
    print("Blad:", e)
