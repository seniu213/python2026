## 7. Dla dowolnego x sprawdź wynik działań (x > 1 and x < 13) oraz (x != 5 or x < 0)

# Pobieranie liczby od użytkownika
x = float(input("Podaj liczbę x: "))

# Sprawdzanie warunków
warunek1 = (x > 1 and x < 13)
warunek2 = (x != 5 or x < 0)

# Wyświetlanie wyników
print(f"Warunek 1 (x > 1 and x < 13): {warunek1}")
print(f"Warunek 2 (x != 5 or x < 0): {warunek2}")