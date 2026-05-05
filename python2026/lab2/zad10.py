# Zadanie 10: wczytuj dwie liczby calkowite, licz iloczyn x*y i zakoncz program gdy x lub y jest rowne 0.
while True:
    x_text = input("Podaj liczbe x (0 konczy program): ")
    y_text = input("Podaj liczbe y (0 konczy program): ")

    if x_text.lstrip("-").isdigit() == False or y_text.lstrip("-").isdigit() == False:
        print("Dozwolone sa tylko liczby calkowite. Sprobuj ponownie.")
        continue

    x = int(x_text)
    y = int(y_text)

    if x == 0 or y == 0:
        print("Koniec programu.")
        break

    result = x * y
    print("Iloczyn", x, "*", y, "=", result)
