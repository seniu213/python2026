wynik = filter(lambda x: x % 7 == 0 and x % 5 != 0, range(2000, 3201))
print(','.join(map(str, wynik)))
