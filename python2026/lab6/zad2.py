import csv
import os
import pickle


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CSV_PATH = os.path.join(DATA_DIR, "movies.csv")
PICKLE_PATH = os.path.join(DATA_DIR, "best_bw_movie.pkl")


def znajdz_film(path_csv, path_pickle):
    try:
        najlepszy_tytul = None
        najlepszy_budzet = -1.0

        with open(path_csv, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                color = (row.get("color") or "").strip().lower()
                budget_txt = (row.get("budget") or "").replace("$", "").replace(",", "").strip()
                title = (row.get("movie_title") or row.get("title") or "").strip()

                if "black and white" not in color or not title or not budget_txt:
                    continue

                try:
                    budget = float(budget_txt)
                except ValueError:
                    continue

                if budget > najlepszy_budzet:
                    najlepszy_budzet = budget
                    najlepszy_tytul = title

        if najlepszy_tytul is None:
            raise ValueError("Brak filmu czarno-bialego z poprawnym budzetem.")

        with open(path_pickle, "wb") as f:
            pickle.dump(najlepszy_tytul, f)

        print("Najlepszy film:", najlepszy_tytul)
        print("Plik pickle:", path_pickle)
        return najlepszy_tytul

    except FileNotFoundError:
        print("Blad: nie znaleziono data/movies.csv")
    except Exception as e:
        print("Blad:", e)


znajdz_film(CSV_PATH, PICKLE_PATH)
