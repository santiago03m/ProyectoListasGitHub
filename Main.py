from Interfaz import *
from ttkthemes import ThemedTk
def main():
    root = ThemedTk(theme="scidblue")
    root.iconbitmap("imagenes/directory_call_telephone_phone_contacts_communication_contact_book_address_icon_210815.ico")
    root.geometry("500x350")
    root.title("Libreta contactos")
    

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    libreta = Libreta()
    contactos_frame = InterfazContactos(master=root, libreta = libreta)
    logica_frame = InterfazLogica(contactos_frame, libreta, master = root)
    

    root.mainloop()

if __name__ == "__main__":
    main()