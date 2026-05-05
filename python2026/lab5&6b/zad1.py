########################## Zadanie 1 #########################
## Utwórz funkcję która będzie zmieniała bieżący katalog dyskowy na inny wskazany przez
## użytkownika (nazwa ścieżki do katalogu to argument wejściowy funkcji)
## oraz będzie wyświetlała zawartość wskazanego przez użytkownika katalogu.
import os


def zmien_katalog_i_pokaz(sciezka):
    os.chdir(sciezka)


    print("Biezacy katalog:", os.getcwd())
    print("Zawartosc katalogu:")
    for element in os.listdir("."):
        print(element)



