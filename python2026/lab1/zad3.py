######################Zadanie 3
# Do poprzednio utworzonego słownika dodaj nowy klucz o nazwie "kierunek_studiów", wartość w/w klucza dowolna
# wskazana przez użytkownika

# Tworzenie słownika z danymi osobowymi
dane = {
    'imie': ['Jan', 'Maria', 'Piotr'],
    'nazwisko': ['Kowalski', 'Nowak', 'Lewandowski'],
    'wiek': [25, 30, 35]
}

# Pobieranie kierunku studiów od użytkownika i dodanie do słownika
kierunek = input("Podaj kierunek studiów: ")
dane['kierunek_studiów'] = kierunek

# Wyświetlanie dostępnych osób
print("Dostępne osoby:")
for i in range(len(dane['imie'])):
    print(f"{i}: {dane['imie'][i]} {dane['nazwisko'][i]}, wiek: {dane['wiek'][i]}")

# Pobieranie numeru od użytkownika
numer = int(input("\nPodaj numer osoby (0-2): "))

# Walidacja numeru
if 0 <= numer < len(dane['imie']):
    print(f"\nDane osoby nr {numer}:")
    print(f"Imię: {dane['imie'][numer]}")
    print(f"Nazwisko: {dane['nazwisko'][numer]}")
    print(f"Wiek: {dane['wiek'][numer]}")
else:
    print("Błąd: Nieprawidłowy numer!")

