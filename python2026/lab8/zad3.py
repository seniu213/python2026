from tkinter import *
from tkinter.messagebox import showinfo, showwarning


def pokaz_wynik():
    odpowiedzi = []

    wybrane1 = []
    if q1_agd.get() == 1:
        wybrane1.append("agd")
    if q1_kosmetyki.get() == 1:
        wybrane1.append("kosmetyki")
    if q1_odziez.get() == 1:
        wybrane1.append("odziez")
    if wybrane1:
        odpowiedzi.append("Dla rodziny: " + ", ".join(wybrane1))

    wybrane2 = []
    if q2_slodycze.get() == 1:
        wybrane2.append("slodycze")
    if q2_ksiazki.get() == 1:
        wybrane2.append("ksiazki")
    if q2_bony.get() == 1:
        wybrane2.append("bony")
    if wybrane2:
        odpowiedzi.append("Dla znajomych: " + ", ".join(wybrane2))

    wybrane3 = []
    if q3_elektronika.get() == 1:
        wybrane3.append("elektronika")
    if q3_sport.get() == 1:
        wybrane3.append("sport")
    if q3_dom.get() == 1:
        wybrane3.append("dom")
    if wybrane3:
        odpowiedzi.append("Dla siebie: " + ", ".join(wybrane3))

    if not odpowiedzi:
        showwarning("Ankieta", "Nie zaznaczono odpowiedzi.")
    else:
        showinfo("Wynik ankiety", "\n".join(odpowiedzi))


window = Tk()
window.title("Ankieta swiateczna")
window.geometry("520x420")

Label(window, text="Co najczesciej kupujesz dla rodziny w prezencie?").grid(row=0, column=0, sticky=W, padx=10, pady=6)
q1_agd = IntVar()
q1_kosmetyki = IntVar()
q1_odziez = IntVar()
Checkbutton(window, text="agd", variable=q1_agd).grid(row=1, column=0, sticky=W, padx=20)
Checkbutton(window, text="kosmetyki", variable=q1_kosmetyki).grid(row=2, column=0, sticky=W, padx=20)
Checkbutton(window, text="odziez", variable=q1_odziez).grid(row=3, column=0, sticky=W, padx=20)

Label(window, text="Co kupujesz dla znajomych?").grid(row=4, column=0, sticky=W, padx=10, pady=6)
q2_slodycze = IntVar()
q2_ksiazki = IntVar()
q2_bony = IntVar()
Checkbutton(window, text="slodycze", variable=q2_slodycze).grid(row=5, column=0, sticky=W, padx=20)
Checkbutton(window, text="ksiazki", variable=q2_ksiazki).grid(row=6, column=0, sticky=W, padx=20)
Checkbutton(window, text="bony", variable=q2_bony).grid(row=7, column=0, sticky=W, padx=20)

Label(window, text="Co kupujesz dla siebie?").grid(row=8, column=0, sticky=W, padx=10, pady=6)
q3_elektronika = IntVar()
q3_sport = IntVar()
q3_dom = IntVar()
Checkbutton(window, text="elektronika", variable=q3_elektronika).grid(row=9, column=0, sticky=W, padx=20)
Checkbutton(window, text="sport", variable=q3_sport).grid(row=10, column=0, sticky=W, padx=20)
Checkbutton(window, text="dom", variable=q3_dom).grid(row=11, column=0, sticky=W, padx=20)

Button(window, text="Pokaz wynik", command=pokaz_wynik).grid(row=12, column=0, pady=15)

window.mainloop()
