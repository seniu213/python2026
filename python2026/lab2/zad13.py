# Zadanie 13: uprosc kod z zadania 11, stosujac jednolinijkowe if/else.
passwords = ("python123", "lab_haslo")
my_name = "Jan Kowalski"

print(my_name) if input("Podaj haslo: ") in passwords else print("Bledne haslo.")

