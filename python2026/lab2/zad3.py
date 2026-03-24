# Zadanie 3: dla dlugiego tekstu policz slowo Emma, zamien tekst na wielkie litery, podziel na wyrazy i policz zdania.
import re

text = """
Emma pracowala nad artykulem o sztucznej inteligencji i porownywala styl czlowieka z komputerem.
W pierwszym akapicie Emma opisala emocje czytelnikow i to, jak szybko rozpoznaja naturalny jezyk.
W drugim akapicie Emma skupila sie na faktach i przytoczyla przyklady z redakcji.
Na koncu Emma napisala, ze najlepszy tekst powstaje wtedy, gdy czlowiek i AI wspolpracuja.
"""

count_emma = len(re.findall(r"\bEmma\b", text))
upper_text = text.upper()
words = text.split()
sentence_count = len([s for s in re.split(r"[.!?]+", text) if s.strip()])

print("a) Liczba wystapien slowa 'Emma':", count_emma)
print("b) Tekst wielkimi literami:")
print(upper_text)
print("c) Lista wyrazow:")
print(words)
print("d) Liczba zdan:", sentence_count)

