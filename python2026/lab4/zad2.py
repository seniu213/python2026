##### Task 2
### Utwórz listę zawierającą 10000 losowych liczb
### wyselekcjonuj liczby mniejsze niż 3 i parzyste
### Wykorzystaj filter() i funkcje z modułu operators

from random import randrange
import operator

l1 = [randrange(1, 100) for _ in range(1000)]

print(list(filter(lambda x:  operator.iand(operator.lt(x, 3), operator.eq(operator.mod(x, 2), 0)), l1)))
