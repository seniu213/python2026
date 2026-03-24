# Zadanie 5: wyznacz ocene koncowa z laboratorium na podstawie procentu punktow z kolokwium (instrukcja match).
points = int(input("Podaj liczbe punktow (0-15): "))

if not 0 <= points <= 15:
    print("Niepoprawna liczba punktow.")
else:
    percent = (points / 15) * 100

    match percent:
        case p if 91 <= p <= 100:
            grade = 5.0
        case p if 81 <= p < 91:
            grade = 4.5
        case p if 71 <= p < 81:
            grade = 4.0
        case p if 61 <= p < 71:
            grade = 3.5
        case p if 50 <= p < 61:
            grade = 3.0
        case _:
            grade = 2.0

    print(f"Wynik: {percent:.2f}%")
    print(f"Ocena koncowa: {grade}")

