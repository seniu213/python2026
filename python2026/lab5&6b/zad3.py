
########################## Zadanie 3 #######################
## W swoim folderze roboczym (w którym masz plik programu) utworz folder o nazwie Dokument,
## do w/w folderu przekopiuj lub utwórz 3 dowolne pliki z rozszerzeniem *.doc np. (Lab1.doc, Lab2.doc, Lab3.doc)
## następnie wykonaj następujące zadania:
## a) korzystając z instrukcji Pythona wyświetl wszystkie pliki znajdujące się folderze roboczym
## b) korzystając z metod Pythona i (pętli lub funkcji filter) wyświetl tylko pliki z rozszerzeniem *.doc znajdujące się folderze roboczym
import os


folder = "Dokument"
os.makedirs(folder, exist_ok=True)

with open(os.path.join(folder, "Lab1.doc"), "w", encoding="utf-8") as f:
    f.write("Plik 1")
with open(os.path.join(folder, "Lab2.doc"), "w", encoding="utf-8") as f:
    f.write("Plik 2")
with open(os.path.join(folder, "Lab3.doc"), "w", encoding="utf-8") as f:
    f.write("Plik 3")

print("Wszystkie pliki w folderze Dokument:")
for nazwa in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, nazwa)):
        print(nazwa)

print("\nTylko .doc:")
for nazwa in os.listdir(folder):
    if nazwa.endswith(".doc"):
        print(nazwa)
