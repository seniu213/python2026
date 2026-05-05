# Zadanie 5: wyznacz ocene koncowa z laboratorium na podstawie procentu punktow z kolokwium.
points = int(input("Podaj liczbe punktow (0-15): "))

if points < 0 or points > 15:
    print("Niepoprawna liczba punktow.")
else:
    percent = (points / 15) * 100

    if percent >= 91:
        grade = 5.0
    elif percent >= 81:
        grade = 4.5
    elif percent >= 71:
        grade = 4.0
    elif percent >= 61:
        grade = 3.5
    elif percent >= 50:
        grade = 3.0
    else:
        grade = 2.0

    print("Wynik:", round(percent, 2), "%")
    print("Ocena koncowa:", grade)
