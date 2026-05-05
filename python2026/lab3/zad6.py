import sil


n = int(input('Podaj n: '))
k = int(input('Podaj k: '))

if n < 0 or k < 0 or k > n:
    print('Bledne dane')
else:
    wynik = sil.silnia(n) // (sil.silnia(k) * sil.silnia(n - k))
    print('Symbol Newtona:', wynik)
