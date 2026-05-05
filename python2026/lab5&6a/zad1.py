# # ################################ Task 1
## A website requires the users to input username and password to register. 
## Create function to check the validity of password input by users.
## Using continue() or break().
## Following are the criteria for checking the password:
## 1. At least 1 letter between [a-z]
## 2. At least 1 number between [0-9]
## 3. At least 1 letter between [A-Z]
## 4. Minimum length of transaction password: 4
## 5. Maximum length of transaction password: 8
## You should to document your code by using python docstrings (google)
## Save result to *.txt file


def is_valid_password(password):
    """Sprawdza haslo."""
    if len(password) < 4 or len(password) > 8:
        return False

    has_lower = False
    has_upper = False
    has_digit = False

    for ch in password:
        if ch.islower():
            has_lower = True
            continue
        if ch.isupper():
            has_upper = True
            continue
        if ch.isdigit():
            has_digit = True

    return has_lower and has_upper and has_digit


def check_passwords(password_line):
    """Zwraca poprawne hasla."""
    valid = []
    for raw in password_line.split(','):
        password = raw.strip()
        if not password:
            continue
        if is_valid_password(password):
            valid.append(password)
    return valid


password_line = 'ABd1234,abcD1,aB1,ABC12ab,z12Qwe,toolongPASS1'
valid_passwords = check_passwords(password_line)

with open('zad1_result.txt', 'w', encoding='utf-8') as file:
    file.write(','.join(valid_passwords))

print('Poprawne hasla:', valid_passwords)
