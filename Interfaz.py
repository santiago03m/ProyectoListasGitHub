import tkinter as tk
from Contacto import Contacto
from Libreta import Libreta
class InterfazLogica(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack(side="left", fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        frame_agregar = tk.Frame(self)
        frame_agregar.pack(padx=10, pady=10)

        label_nombre = tk.Label(frame_agregar, text="Nombre:")
        label_nombre.grid(row=0, column=0, padx=5, pady=5)

        self.entry_nombre = tk.Entry(frame_agregar)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        label_telefono = tk.Label(frame_agregar, text="Teléfono:")
        label_telefono.grid(row=1, column=0, padx=5, pady=5)

        self.entry_telefono = tk.Entry(frame_agregar)
        self.entry_telefono.grid(row=1, column=1, padx=5, pady=5)

        boton_agregar = tk.Button(frame_agregar, text="Agregar", command=self.agregar_contacto)
        boton_agregar.grid(row=2, columnspan=2, padx=5, pady=5)

    def agregar_contacto(self, libreta):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        contacto = Contacto(nombre, telefono)
        libreta.guardar_contacto(contacto)

class InterfazContactos(tk.Frame):
    def __init__(self, master=None, libreta = None):
        super().__init__(master)
        self.master = master
        self.libreta = libreta
        self.pack(side="right", fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.lista_contactos = tk.Listbox(self)
        self.lista_contactos.pack(side="top", fill="both", expand=True)

        self.boton_modificar = tk.Button(self, text="Modificar", command=self.modificar_contacto)
        self.boton_modificar.pack(side="bottom", pady=5)

        self.actualizar_lista_contactos()

    def actualizar_lista_contactos(self):
        self.lista_contactos.delete(0, tk.END)
        for i, contacto in enumerate(self.libreta.libreta):
            self.lista_contactos.insert(tk.END, f"{i + 1}. {contacto.nombre} - {contacto.numero}")

    def modificar_contacto(self):
        seleccionado = self.lista_contactos.curselection()
        if seleccionado:
            indice = seleccionado[0]


def main():
    root = tk.Tk()
    root.geometry("1000x800")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    libreta = Libreta()
    logica_frame = InterfazLogica(master = root)
    contactos_frame = InterfazContactos(master=root, libreta = libreta)

    root.mainloop()

if __name__ == "__main__":
    main()
