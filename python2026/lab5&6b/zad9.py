import os


tekst = (
    "Python jest prosty. "
    "To jest drugie zdanie. "
    "To jest trzecie zdanie. "
    "To jest czwarte zdanie. "
    "To jest piate zdanie. "
    "To jest szoste zdanie."
)

folder = "TekstyZad9"
os.makedirs(folder, exist_ok=True)

nazwy = [
    "Tekst1ID_ABC",
    "Tekst2ID_405.txt",
    "Tekst3ID_607.txt",
    "Tekst4ID_ABC.txt",
    "Tekst5ID_DEF.txt",
]

for nazwa in nazwy:
    with open(os.path.join(folder, nazwa), "w", encoding="utf-8") as f:
        f.write(tekst)


def lista_plikow_i_abc(folder_name):
    wszystkie = []
    abc_info = {}

    for nazwa in os.listdir(folder_name):
        sciezka = os.path.join(folder_name, nazwa)
        if not os.path.isfile(sciezka):
            continue

        wszystkie.append(nazwa)

        if "ID_ABC" in nazwa:
            with open(sciezka, "r", encoding="utf-8") as f:
                slowa = f.read().replace(".", " ").split()
            licznik = 0
            for slowo in slowa:
                if len(slowo) >= 3:
                    licznik += 1
            abc_info[nazwa] = licznik

    return wszystkie, abc_info


def analiza(folder_name):
    wszystkie, abc_info = lista_plikow_i_abc(folder_name)

    ile_z_0 = 0
    bez_0 = {}

    for nazwa in wszystkie:
        po_id = nazwa.split("ID_")[-1]
        if "0" in po_id:
            ile_z_0 += 1
        else:
            with open(os.path.join(folder_name, nazwa), "r", encoding="utf-8") as f:
                slowa = f.read().replace(".", " ").split()
            licznik = 0
            for slowo in slowa:
                if len(slowo) >= 3:
                    licznik += 1
            bez_0[nazwa] = licznik

    return ile_z_0, bez_0, abc_info


wszystkie, abc = lista_plikow_i_abc(folder)
print("Wszystkie pliki:")
for x in wszystkie:
    print(x)

print("\nABC:")
for nazwa, liczba in abc.items():
    print(nazwa, "->", liczba)

ile_z_0, bez_0, abc = analiza(folder)
print("\nIle plikow z 0 w ID:", ile_z_0)

print("\nPliki bez 0 w ID:")
for nazwa, liczba in bez_0.items():
    print(nazwa, "->", liczba)

print("\nABC jeszcze raz:")
for nazwa, liczba in abc.items():
    print(nazwa, "->", liczba)
