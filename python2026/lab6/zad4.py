import csv
import os


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CSV_PATH = os.path.join(DATA_DIR, "titanic_train.csv")


def funkcja_wielu_argumentow(*args):
    try:
        if len(args) == 1 and isinstance(args[0], dict):
            liczby = list(args[0].values())
        elif len(args) == 1 and isinstance(args[0], (list, tuple, set)):
            liczby = list(args[0])
        else:
            liczby = list(args)

        if not liczby:
            raise ValueError("Brak danych.")

        for x in liczby:
            if not isinstance(x, (int, float)):
                raise TypeError("Wszystkie dane musza byc liczbami.")

        for x in liczby:
            if x == 3 or x == -7:
                return x

        raise ValueError("W danych nie ma 3 ani -7.")

    except Exception as e:
        print("Blad:", e)
        return None


assert funkcja_wielu_argumentow(1, 2, 3, 4) == 3

try:
    with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        row = next(reader)

    seq = (int(row["PassengerId"]), int(row["Pclass"]), int(row["Survived"]), int(row["SibSp"]))
    lista = [int(row["Pclass"]), int(row["SibSp"]), int(row["Parch"]), int(row["Survived"])]
    slownik = {"a": int(row["PassengerId"]), "b": int(row["Pclass"])}

    print("Wynik dla sekwencji:", funkcja_wielu_argumentow(*seq))
    print("Wynik dla listy:", funkcja_wielu_argumentow(lista))
    print("Wynik dla slownika:", funkcja_wielu_argumentow(slownik))
except FileNotFoundError:
    print("Blad: nie znaleziono data/titanic_train.csv")
except Exception as e:
    print("Blad:", e)
