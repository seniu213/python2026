# ########################## Task  2
# Przypisz do zmiennej wartość która będzie twoim imieniem i nazwiskiem następnie korzystając
# z funkcji lambda rozdziel wyraz na poszczegolne wyrazy, a potem wyrazy na litery
# użyj funkcji list i metody split - dla zmiennych typu string


name = 'Arseni Zuyevich'
lf = lambda x: name.split(' ')
name = lf(name)
name = list(name[0]) + list(name[1])
print(name)