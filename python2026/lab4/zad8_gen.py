### Task 8
### Utwórz własny generator liczb które są kolejnymi wielokrotnosciami liczby cztery tj. 4,16,32,64,... itd
### n - liczbę elementów w generatorze deklaruje użytkownik
### np. dla n=3,  funkcja next w kolejnych wywołaniach zwraca:  4, 16, 32


def gen(n):
    for i in range(1, n+1):
        yield 4**i

print(list(gen(3)))