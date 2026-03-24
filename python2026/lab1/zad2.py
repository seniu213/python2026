######################Zadanie 2
# Utwórz słownik zawierający  trzy klucze: imie, nazwisko, wiek
# jako wartości w/w kluczy wpisz listy 3-elementowe zawierające dowolne dane osobowe
# następnie wyświetl kompletne dane osoby o numerze wskazanej przez użytkownika

# Tworzenie słownika z danymi osobowymi
dane = {
    'imie': ['Jan', 'Maria', 'Piotr'],
    'nazwisko': ['Kowalski', 'Nowak', 'Lewandowski'],
    'wiek': [25, 30, 35]
}

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
