# ########################## Task 1
# Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
# z funkcji lambda połącz kolejne litery w jeden wyraz (swoje imie)



name  = []
name.extend('Arseni')
func = lambda x: ''.join(x)
name = func(name)


