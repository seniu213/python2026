from tkinter import *
from tkinter.messagebox import showinfo, showerror


def licz():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        op = var.get()

        if op == 1:
            wynik = x + y
        elif op == 2:
            wynik = x - y
        elif op == 3:
            wynik = x * y
        elif op == 4:
            if y == 0:
                raise ZeroDivisionError
            wynik = x / y
        else:
            showerror("Blad", "Wybierz operacje.")
            return

        text_wynik.config(text="Wynik: " + str(wynik))
        showinfo("Wynik", "Wynik: " + str(wynik))
    except ValueError:
        showerror("Blad", "Wpisz liczby.")
    except ZeroDivisionError:
        showerror("Blad", "Nie mozna dzielic przez zero.")
    except TypeError:
        showerror("Blad", "Zly typ danych.")


window = Tk()
window.title("Kalkulator")
window.geometry("360x220")

Label(window, text="Liczba x").grid(row=0, column=0, padx=10, pady=10)
Label(window, text="Liczba y").grid(row=1, column=0, padx=10, pady=10)

entry_x = Entry(window)
entry_x.grid(row=0, column=1, padx=10, pady=10)

entry_y = Entry(window)
entry_y.grid(row=1, column=1, padx=10, pady=10)

var = IntVar()
Radiobutton(window, text="+", variable=var, value=1).grid(row=0, column=2)
Radiobutton(window, text="-", variable=var, value=2).grid(row=1, column=2)
Radiobutton(window, text="*", variable=var, value=3).grid(row=2, column=2)
Radiobutton(window, text="/", variable=var, value=4).grid(row=3, column=2)

Button(window, text="ok", command=licz).grid(row=4, column=1, pady=10)

text_wynik = Label(window, text="Wynik: ")
text_wynik.grid(row=5, column=0, columnspan=3, pady=10)

window.mainloop()
