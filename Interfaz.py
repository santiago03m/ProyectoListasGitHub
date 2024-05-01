import tkinter as tk
from Contacto import Contacto
from Libreta import Libreta
class InterfazLogica(tk.Frame):
    def __init__(self, interfaz_contactos, libreta: Libreta, master = None):
        super().__init__(master)
        self.interfaz_contactos = interfaz_contactos
        self.master = master
        self.libreta = libreta
        self.pack(side="left", fill="both", expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        estilo_widget = {"borderwidth": 1, "highlightthickness": 0}
        frame_agregar = tk.Frame(self)
        frame_agregar.pack(padx=10, pady=10)

        label_nombre = tk.Label(frame_agregar, text="Nombre:")
        label_nombre.grid(row=0, column=0, padx=5, pady=5)

        self.entry_nombre = tk.Entry(frame_agregar, **estilo_widget)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        label_telefono = tk.Label(frame_agregar, text="Teléfono:")
        label_telefono.grid(row=1, column=0, padx=5, pady=5)

        self.entry_telefono = tk.Entry(frame_agregar, **estilo_widget)
        self.entry_telefono.grid(row=1, column=1, padx=5, pady=5)

        boton_agregar = tk.Button(frame_agregar, text="Agregar", command=self.agregar_contacto, **estilo_widget)
        boton_agregar.grid(row=2, columnspan=2, padx=5, pady=5)

    def agregar_contacto(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        contacto = Contacto(nombre, telefono)
        self.libreta.guardar_contacto(contacto)
        self.entry_nombre.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.interfaz_contactos.actualizar_lista_contactos()


class InterfazContactos(tk.Frame):
    def __init__(self, master=None, libreta: Libreta = None):
        super().__init__(master)
        self.master = master
        self.libreta = libreta
        self.pack(side="right", fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        estilo_widget = {"borderwidth": 1, "highlightthickness": 0}
        self.lista_contactos = tk.Listbox(self)
        self.lista_contactos.pack(side="top", fill="both", expand=True)

        self.boton_modificar = tk.Button(self, text="Modificar", command=self.modificar_contacto, **estilo_widget)
        self.boton_modificar.pack(side="bottom", pady=5)
        
        self.boton_modificar = tk.Button(self, text="Eliminar", command=self.eliminar_contacto, **estilo_widget)
        self.boton_modificar.pack(side="bottom", pady=5)

        self.actualizar_lista_contactos()

    def actualizar_lista_contactos(self):
        self.lista_contactos.delete(0, tk.END)  # Limpiar la lista antes de actualizarla
        if self.libreta:
            for i, contacto in enumerate(self.libreta.libreta):
                self.lista_contactos.insert(tk.END, f"{i + 1}. {contacto.nombre} - {contacto.numero}")
    
    
    def eliminar_contacto(self):
        seleccionado = self.lista_contactos.curselection()
        if seleccionado:
            indice = seleccionado[0]
            del self.libreta.libreta[indice]
            self.actualizar_lista_contactos()

    def modificar_contacto(self):
        seleccionado = self.lista_contactos.curselection()
        if seleccionado:
            estilo_widget = {"borderwidth": 1, "highlightthickness": 0}
            indice = seleccionado[0]
            ventana_modificar = tk.Toplevel(self)
            ventana_modificar.title("Modificar contacto")
            ventana_modificar.geometry("400x400")

            label_nombre = tk.Label(ventana_modificar, text="Nuevo nombre:")
            label_nombre.grid(row=0, column=0, padx=5, pady=5)
            entry_nuevo_nombre = tk.Entry(ventana_modificar, **estilo_widget)
            entry_nuevo_nombre.grid(row=0, column=1, padx=5, pady=5)

            label_telefono = tk.Label(ventana_modificar, text="Nuevo teléfono:")
            label_telefono.grid(row=1, column=0, padx=5, pady=5)
            entry_nuevo_telefono = tk.Entry(ventana_modificar, **estilo_widget)
            entry_nuevo_telefono.grid(row=1, column=1, padx=5, pady=5)

            boton_guardar = tk.Button(ventana_modificar, text="Guardar", command = lambda: self.guardar_modificacion(indice, entry_nuevo_nombre.get(), entry_nuevo_telefono.get(), ventana_modificar), **estilo_widget)
            boton_guardar.grid(row=2, columnspan=2, padx=5, pady=5)

    def guardar_modificacion(self, indice, nuevo_nombre, nuevo_telefono, ventana_modificar):
        contacto_modificado = self.libreta.libreta[indice]
        contacto_modificado.nombre = nuevo_nombre
        contacto_modificado.numero = nuevo_telefono
        ventana_modificar.destroy()
        self.actualizar_lista_contactos()