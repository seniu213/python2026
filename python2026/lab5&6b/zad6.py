import pickle


lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista3 = [10, 20, 30]

with open("listy.pkl", "wb") as f:
    pickle.dump([lista1, lista2, lista3], f)

del lista1
del lista2
del lista3

with open("listy.pkl", "rb") as f:
    lista1, lista2, lista3 = pickle.load(f)

print(lista1)
print(lista2)
print(lista3)
