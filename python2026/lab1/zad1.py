# #Zadanie 1
# Utwórz listę z imionami (conajmniej 10 imion, część powinna się powtarzać)
# określ indeks (numer wiersza) w której znajduje się imie osoby, nazwę osoby podaje użytkownik
# ile osób o imieniu wskazanym przez użytkownika znajduje się na liście
# dołącz nowe imie do listy do końca listy
# dołącz nowe imię jako 3 pozycję na liście
# posortuj obiekty w liście, usuń ostatni element z listy
# utwórz nową listę z 3 imionami i dołącz do listy


lista = ['Arseni', 'Erwin', 'Bartek', 'Alicja', 'Bob', 'Artem', 'Erwin', 'Bartek', 'Imie9', 'Imie10']
wybor_uzytkownika = input()
print(lista.index(wybor_uzytkownika), lista.count(wybor_uzytkownika), sep='\n')
lista.append('Imie11')
lista.insert(3, 'qwe')
lista.sort()
del lista[-1]
lista + ['im1', 'im2', 'im3']
