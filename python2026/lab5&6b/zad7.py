from struct import pack, unpack


liczba = 123456789

with open("liczba.dat", "wb") as f:
    f.write(pack("i", liczba))

with open("liczba.dat", "rb") as f:
    wynik = unpack("i", f.read())[0]

print("zapis:", liczba)
print("odczyt:", wynik)
