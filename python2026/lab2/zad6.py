# Zadanie 6: oblicz sume ciagu 1 + 1/2 + 1/3 + ... + 1/m uzywajac petli for i danych od uzytkownika.
m = int(input("Podaj m (m > 0): "))

if m <= 0:
    print("m musi byc dodatnie.")
else:
    sequence_sum = 0.0
    for i in range(1, m + 1):
        sequence_sum += 1 / i
    print(f"Suma ciagu 1 + 1/2 + ... + 1/{m} = {sequence_sum:.6f}")

