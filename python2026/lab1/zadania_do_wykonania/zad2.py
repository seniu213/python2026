## 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)

# Pobieranie wartości x i y od użytkownika
x = float(input("Podaj wartość x: "))
y = float(input("Podaj wartość y: "))

# Obliczanie wyniku wyrażenia 2x+5y
wynik = 2 * x + 5 * y

# Wyświetlanie wyniku
print(f"Wynik wyrażenia 2x+5y dla x={x} i y={y} to: {wynik}")