#### Zadanie 10
## Porownaj czas obliczen i zuzycie pamieci dla 4 podejsc:
## a) imperatywnie/strukturalnie,
## b) funkcyjnie z funkcjami, ale bez funkcji wyzszego rzedu,
## c) funkcyjnie z funkcjami wyzszego rzedu,
## d) funkcyjnie z generatorem/iteratorem.
## Utworz 3 listy po 1_000_000 losowych liczb.
## Przepisz liczby z 3 list do 2 list:
## pierwsza lista ma liczby parzyste, druga ma liczby nieparzyste.
## Wskaz, ktory wariant jest najszybszy i ktory zuzywa najmniej pamieci.

from random import randint
from itertools import chain
from datetime import datetime
from sys import getsizeof

N = 1_000_000

list1 = [randint(1, 1_000_000) for _ in range(N)]
list2 = [randint(1, 1_000_000) for _ in range(N)]
list3 = [randint(1, 1_000_000) for _ in range(N)]
all_lists = [list1, list2, list3]


def memory_size(even_list, odd_list):
    return getsizeof(even_list) + getsizeof(odd_list)


# a) imperatywnie
def variant_a(data):
    even = []
    odd = []
    for part in data:
        for x in part:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
    return even, odd


# b) funkcje
def put_number(x, even, odd):
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)


def variant_b(data):
    even = []
    odd = []
    for part in data:
        for x in part:
            put_number(x, even, odd)
    return even, odd


# c) wyzszy rzad
def variant_c(data):
    even_parts = map(lambda arr: list(filter(lambda x: x % 2 == 0, arr)), data)
    odd_parts = map(lambda arr: list(filter(lambda x: x % 2 != 0, arr)), data)

    even = list(chain.from_iterable(even_parts))
    odd = list(chain.from_iterable(odd_parts))
    return even, odd


# d) generator
def variant_d(data):
    even = list(x for x in chain.from_iterable(data) if x % 2 == 0)
    odd = list(x for x in chain.from_iterable(data) if x % 2 != 0)
    return even, odd


def benchmark(name, func, data):
    t0 = datetime.now()
    even, odd = func(data)
    dt = (datetime.now() - t0).total_seconds()
    mem = memory_size(even, odd)

    print(name)
    print('czas [s]:', round(dt, 4))
    print('pamiec [B]:', mem)
    print('parzyste:', len(even), 'nieparzyste:', len(odd))
    print('-' * 40)

    return name, dt, mem


results = []
results.append(benchmark('a) imperatywnie', variant_a, all_lists))
results.append(benchmark('b) funkcje', variant_b, all_lists))
results.append(benchmark('c) wyzszy rzad', variant_c, all_lists))
results.append(benchmark('d) generator', variant_d, all_lists))

fastest = min(results, key=lambda x: x[1])
smallest = min(results, key=lambda x: x[2])

print('Najszybciej:', fastest[0])
print('Najmniej pamieci:', smallest[0])
