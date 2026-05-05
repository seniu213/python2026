# Zadanie 13: wersja zadania 11 napisana bardziej podstawowo.
password1 = "python123"
password2 = "lab_haslo"
my_name = "Jan Kowalski"

entered = input("Podaj haslo: ")

if entered == password1 or entered == password2:
    print(my_name)
else:
    print("Bledne haslo.")
