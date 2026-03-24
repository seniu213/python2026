# ########################## Task 4
## Utwórz dwie listy, do każdej z nich niezależnie zapisuj odpowiednio
## podawane przez użytkowników login (pierwsza lista) i hasło (druga lista),
## operacja zapisu jest powtarzana aż do momentu wpisania przez użytkownika "STOP"
## użyj break, continue, enumerate().
## Następnie login-y i hasła zapisz do słownika (login to klucz słownika).


logins = []
passwords = []
login = ''
password = ''

while(True):
    login = input()
    if login == 'STOP':
        break
    password = input()
    if password == 'STOP':
        break
    logins.append(login)
    passwords.append(password)


d = {}
for log, pas in zip(logins, passwords):
    d[log] = pas

print(d)