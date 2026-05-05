########################## Zadanie 2 #########################
## Korzystając z utworzonej funkcji napisz funkcję która będzie zmieniała bieżący katalog
## dyskowy na inny wskazany przez użytkownika oraz będzie wyświetlała zawartość wskazanego przez
## użytkownika katalogu.
## Przetestuj działanie programu dla natepującego przypadku:
## program działa tylko wówczas gdy użytkownik odpowie "yes" na pytanie:
## "Czy mam zmienić katalog?", zastosuj pętle while True(zmuś użytkownika :) do wpisania "yes")
import os


def zmien_katalog_i_pokaz(sciezka):

    os.chdir(sciezka)


    print("Biezacy katalog:", os.getcwd())
    print("Zawartosc katalogu:")
    for element in os.listdir("."):
        print(element)


def wymus_yes():
    while True:
        odpowiedz = input("Czy mam zmienic katalog? ")
        if odpowiedz == "yes":
            return
        print("Wpisz dokladnie: yes")



wymus_yes()
sciezka = input("Podaj sciezke do katalogu: ").strip()
zmien_katalog_i_pokaz(sciezka)
