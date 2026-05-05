##### Task 4
### Utwórz funkcję funcycle(n) która z sekwencji 'INFORMATYKA'
### n krotnie (argument funkcji) wypisze w cyklu każdy z jej elementów
### Wykorzystaj cycle()



def funcycle(n):
    from itertools import cycle
    s = 'INFORMATYKA'
    i = 0
    for j in cycle(s):
        if i == 11: break
        for _ in range(n):
            print(j, end='')
        print()
        i += 1


funcycle(2)
