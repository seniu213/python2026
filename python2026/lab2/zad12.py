# Zadanie 12: wygeneruj 100 liczb losowych i wypisz liczby nieparzyste/parzyste posortowane rosnaco.
import random

numbers = [random.randint(0, 1000) for _ in range(100)]
odd_sorted = sorted([n for n in numbers if n % 2 == 1])
even_sorted = sorted([n for n in numbers if n % 2 == 0])

print("Wylosowana lista:")
print(numbers)
print()

print("Nieparzyste rosnaco:")
print(odd_sorted)
print()

print("Parzyste rosnaco:")
print(even_sorted)

