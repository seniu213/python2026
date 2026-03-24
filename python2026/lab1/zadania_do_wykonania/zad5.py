## 6. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
## iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.



# Pobieranie dwóch liczb od użytkownika
num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))

# Obliczanie sumy, różnicy, iloczynu, ilorazu i potęgi
suma = num1 + num2
roznica = num1 - num2
iloczyn = num1 * num2
iloraz = num1 / num2 if num2 != 0 else "Nie można dzielić przez zero"
potega = num1 ** num2
# Wyświetlanie wyników
print(f"Suma: {suma}")
print(f"Różnica: {roznica}")
print(f"Iloczyn: {iloczyn}")
print(f"Iloraz: {iloraz}")
print(f"Potęga: {potega}")







