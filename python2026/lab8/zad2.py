from tkinter import *
from tkinter.messagebox import showerror


def policz_rate():
    try:
        k = float(entry_kwota.get())
        n = var_n.get()

        if k < 1000 or k > 10000:
            showerror("Blad", "Kwota musi byc od 1000 do 10000.")
            return
        if n not in [1, 2, 3]:
            showerror("Blad", "Wybierz liczbe okresow.")
            return

        p = 5.0
        q = 1 + p / 100
        rata = (k * (q ** n) * (1 - q)) / (1 - (q ** n))

        if rata < 3500:
            kolor = "green"
        elif rata < 7000:
            kolor = "orange"
        else:
            kolor = "red"

        wynik.config(text="Rata: " + str(round(rata, 2)) + " zl", fg=kolor)
    except ValueError:
        showerror("Blad", "Wpisz poprawna kwote.")
    except TypeError:
        showerror("Blad", "Zly typ danych.")


window = Tk()
window.title("Rata kredytu")
window.geometry("420x240")

Label(window, text="Kwota kredytu 1000-10000").grid(row=0, column=0, padx=10, pady=10, sticky=W)
entry_kwota = Entry(window)
entry_kwota.grid(row=0, column=1, padx=10, pady=10)

Label(window, text="Liczba okresow n").grid(row=1, column=0, padx=10, pady=10, sticky=W)
var_n = IntVar()
Radiobutton(window, text="1", variable=var_n, value=1).grid(row=1, column=1, sticky=W)
Radiobutton(window, text="2", variable=var_n, value=2).grid(row=2, column=1, sticky=W)
Radiobutton(window, text="3", variable=var_n, value=3).grid(row=3, column=1, sticky=W)

Label(window, text="p = 5%").grid(row=4, column=0, padx=10, pady=5, sticky=W)

Button(window, text="Oblicz", command=policz_rate).grid(row=5, column=1, pady=10)

wynik = Label(window, text="Rata: ", font=("Arial", 13))
wynik.grid(row=6, column=0, columnspan=2, pady=10)

window.mainloop()
