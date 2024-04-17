from interfaz.Interfaz import Interfaz
import tkinter as tk

def main():
    ventana=tk.Tk()
    ventanaInterfaz=Interfaz(ventana)
    ventana.mainloop()


if __name__ == '__main__':
    main()