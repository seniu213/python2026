# Zadanie 12: wygeneruj 100 liczb losowych i wypisz liczby nieparzyste/parzyste posortowane rosnaco.
import random

numbers = []
for i in range(100):
    random_number = random.randint(0, 1000)
    numbers.append(random_number)

odd_sorted = []
even_sorted = []

for number in numbers:
    if number % 2 == 0:
        even_sorted.append(number)
    else:
        odd_sorted.append(number)

odd_sorted.sort()
even_sorted.sort()

print("Wylosowana lista:")
print(numbers)
print()

print("Nieparzyste rosnaco:")
print(odd_sorted)
print()

print("Parzyste rosnaco:")
print(even_sorted)
