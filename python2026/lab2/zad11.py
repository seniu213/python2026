# Zadanie 11: wyswietl imie i nazwisko po podaniu poprawnego hasla (jednego z dwoch z krotki).
passwords = ("python123", "lab_haslo")
my_name = "Jan Kowalski"

entered = input("Podaj haslo: ")

if entered in passwords:
    print(my_name)
else:
    print("Bledne haslo.")

