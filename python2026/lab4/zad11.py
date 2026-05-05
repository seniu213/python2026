#### Zadanie 11
## Dla duzych danych zastosuj algorytm "dziel i rzadz":
## 1) podziel dane na czesci,
## 2) wykonaj mapowanie (np. pary klucz-wartosc),
## 3) przesun/grupuj podobne klucze,
## 4) zredukuj i zagreguj wyniki.
## Utworz liste 10000 losowych nazw 6 jezykow programowania,
## np. ['python','java','C++',...].
## Policz, ile razy wybrany jezyk wystepuje w liscie:
## a) imperatywnie,
## b) funkcyjnie,
## c) z uzyciem "dziel i rzadz".

from random import choice
from functools import reduce

prog_langs = ['python', 'java', 'C++', 'csharp', 'javascript', 'go']
list_prog = [choice(prog_langs) for _ in range(10000)]

search_lang = 'python'


# a) imperatywnie
count_a = 0
for lang in list_prog:
    if lang == search_lang:
        count_a += 1


# b) funkcyjnie
count_b = len(list(filter(lambda x: x == search_lang, list_prog)))


# c) dziel i rzadz
def chunks(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


parts = list(chunks(list_prog, 1000))
mapped_counts = map(lambda part: part.count(search_lang), parts)
count_c = reduce(lambda x, y: x + y, mapped_counts, 0)


print('Szukany jezyk:', search_lang)
print('a) imperatywnie:', count_a)
print('b) funkcyjnie:', count_b)
print('c) dziel i rzadz:', count_c)
