import functools
import operator


wynik = functools.reduce(operator.mul, range(1, 100), 1)
print(wynik)
