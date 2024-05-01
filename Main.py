from Interfaz import *
def main():
    root = tk.Tk()
    root.geometry("1000x700")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    libreta = Libreta()
    contactos_frame = InterfazContactos(master=root, libreta = libreta)
    logica_frame = InterfazLogica(contactos_frame, libreta, master = root)
    

    root.mainloop()

if __name__ == "__main__":
    main()