
########################## Zadanie 4 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze 2 katalogi:
## StudentDoc, StudentObrazy, do w/w folderów zapisz w każdym z nich 2 dowolne
## pliki odpowiednio tekstowe i graficzne, a następnie wyświetl zawartość poszczególnych
## folderów podaj rozmiar każdego pliku
import os


folder_doc = "StudentDoc"
folder_img = "StudentObrazy"

os.makedirs(folder_doc, exist_ok=True)
os.makedirs(folder_img, exist_ok=True)

with open(os.path.join(folder_doc, "a.txt"), "w", encoding="utf-8") as f:
    f.write("tekst 1")
with open(os.path.join(folder_doc, "b.txt"), "w", encoding="utf-8") as f:
    f.write("tekst 2")

with open(os.path.join(folder_img, "a.jpg"), "wb") as f:
    f.write(b"img1")
with open(os.path.join(folder_img, "b.png"), "wb") as f:
    f.write(b"img2")

print("StudentDoc:")
for nazwa in os.listdir(folder_doc):
    sciezka = os.path.join(folder_doc, nazwa)
    if os.path.isfile(sciezka):
        print(nazwa, os.path.getsize(sciezka), "B")

print("\nStudentObrazy:")
for nazwa in os.listdir(folder_img):
    sciezka = os.path.join(folder_img, nazwa)
    if os.path.isfile(sciezka):
        print(nazwa, os.path.getsize(sciezka), "B")
