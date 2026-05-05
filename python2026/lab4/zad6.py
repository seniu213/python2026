### Task 6
### Posiadasz grupę N-studentów (N-indeksów), podziel w/w grupę na n-podgrup
### Specyfikacja kodu: funkcja, wykorzystanie iteratora kombinatorycznego


from itertools import combinations


def f(n, N):
    print(list(combinations(N,n)))

N = list(range(10))
f(3, N)