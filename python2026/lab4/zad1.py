##### Task 1
### Utwórz 2 listy, pierwsza liczby od 1 do 100, druga 100 losowych liczb
### odejmnij wartości elementów listy pierwszej od drugiej
### Wykorzystaj map() i funkcję sub() z modułu operators

from random import randrange
from operator import sub

l1 = [i for i in range(1, 101)]
l2 = [randrange(1, 100) for _ in range(100)]

print(list(map(sub, l1, l2)))
