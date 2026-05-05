def warunek(x):
    if x % 7 == 0 and x % 5 != 0:
        return True
    return False


wynik = filter(warunek, range(2000, 3201))
print(','.join(map(str, wynik)))
