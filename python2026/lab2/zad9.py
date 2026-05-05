# Zadanie 9: znajdz liczby od 1 do 1000, w ktorych kazda cyfra jest parzysta, i wypisz je po przecinku.
result = []

for number in range(1, 1001):
    text_number = str(number)
    all_digits_even = True

    for digit_char in text_number:
        digit = int(digit_char)
        if digit % 2 != 0:
            all_digits_even = False

    if all_digits_even:
        result.append(text_number)

output = ""
for i in range(len(result)):
    output = output + result[i]
    if i < len(result) - 1:
        output = output + ","

print(output)
