# Zadanie 10: wczytuj dwie liczby calkowite, licz iloczyn x*y i zakoncz program gdy x lub y jest rowne 0 (if/for/break/continue).
for _ in range(1_000_000):
    x_raw = input("Podaj liczbe x (0 konczy program): ")
    y_raw = input("Podaj liczbe y (0 konczy program): ")

    if not (x_raw.lstrip("-").isdigit() and y_raw.lstrip("-").isdigit()):
        print("Dozwolone sa tylko liczby calkowite. Sprobuj ponownie.")
        continue

    x = int(x_raw)
    y = int(y_raw)

    if x == 0 or y == 0:
        print("Koniec programu.")
        break

    print(f"Iloczyn {x} * {y} = {x * y}")

