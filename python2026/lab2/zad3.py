# Zadanie 3: dla dlugiego tekstu policz slowo Emma, zamien tekst na wielkie litery, podziel na wyrazy i policz zdania.
text = """
Emma pracowala nad artykulem o sztucznej inteligencji i porownywala styl czlowieka z komputerem.
W pierwszym akapicie Emma opisala emocje czytelnikow i to, jak szybko rozpoznaja naturalny jezyk.
W drugim akapicie Emma skupila sie na faktach i przytoczyla przyklady z redakcji.
Na koncu Emma napisala, ze najlepszy tekst powstaje wtedy, gdy czlowiek i AI wspolpracuja.
"""

words = text.split()
count_emma = 0
for word in words:
    clean_word = word.strip(".,!?;:\"'()")
    if clean_word == "Emma":
        count_emma = count_emma + 1

upper_text = text.upper()

word_list = []
for word in words:
    word_list.append(word)

sentence_count = 0
for sign in text:
    if sign == "." or sign == "!" or sign == "?":
        sentence_count = sentence_count + 1

print("a) Liczba wystapien slowa 'Emma':", count_emma)
print("b) Tekst wielkimi literami:")
print(upper_text)
print("c) Lista wyrazow:")
print(word_list)
print("d) Liczba zdan:", sentence_count)
