# Zadanie 7: oblicz pierwiastki liczb od 1 do 10 korzystajac z petli while.
i = 1

while i <= 10:
    root = i ** 0.5
    print("sqrt(" + str(i) + ") = " + str(round(root, 6)))
    i = i + 1
