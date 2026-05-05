### Task 7
## początkowa kwota na 3mc lokacie to k = 10000, oprocentowanie lokaty to 0.01%
## oblicz jaką kwotę zgromadzi użytkownik po upływie t = 9mc
### Specyfikacja kodu: funkcja, wykorzystanie iteratora skończonego


from itertools import accumulate
import operator

k = 10000
r = 1.0001
t = 9

growth = list(accumulate([r] * t, operator.mul))

result = [k * x for x in growth]

print(result[-1])  # итоговая сумма