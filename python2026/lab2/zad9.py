# Zadanie 9: znajdz liczby od 1 do 1000, w ktorych kazda cyfra jest parzysta, i wypisz je po przecinku.
result = []

for number in range(1, 1001):
    if all(int(digit) % 2 == 0 for digit in str(number)):
        result.append(str(number))

print(",".join(result))

