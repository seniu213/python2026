### Task 9
## a) Utwórz własny generator zwracający 1000 losowych liczb parzystych z zakresu 0-100000000

from random import randrange

def gen():
    for i in range(1000):
        yield randrange(0, 100000000)


print(list(gen()))
