import functools
import operator


silnia = lambda n: functools.reduce(operator.mul, range(1, n + 1), 1)
