########################## Zadanie 5 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze katalog,
## a następnie zmień nazwę katalogu na inną, dowolną.
import os


stary = "MojKatalog"
nowy = "MojNowyKatalog"

if os.path.exists(stary):
    i = 1
    while os.path.exists(f"{stary}{i}"):
        i += 1
    stary = f"{stary}{i}"

if os.path.exists(nowy):
    i = 1
    while os.path.exists(f"{nowy}{i}"):
        i += 1
    nowy = f"{nowy}{i}"

os.mkdir(stary)
os.rename(stary, nowy)

print("Utworzono:", stary)
print("Po zmianie:", nowy)
