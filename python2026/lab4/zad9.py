#### Task 9
## Utwórz generator dla ciągu Fibonacciego (pierwszy wyraz ciągu jest równy 0, drugi jest równy 1,
## a każdy kolejny element ciągu jest sumą dwóch poprzednich. Wypisz n-ty element tego ciągu
## Użytkownik deklaruje ilość elementów (n).
## Specyfikacja: użyj accumulate() lub reduce() do wygenerowania ciągu Fibonacciego

from functools import reduce


def fib_generator(n):
    if n <= 0:
        return
    if n == 1:
        yield 0
        return

    fib_list = reduce(
        lambda acc, _: acc + [acc[-1] + acc[-2]],
        range(n - 2),
        [0, 1]
    )

    for num in fib_list:
        yield num


n = 10
fib_seq = list(fib_generator(n))

print(fib_seq)
print(f"{n}-ty wyraz:", fib_seq[-1] if fib_seq else None)
