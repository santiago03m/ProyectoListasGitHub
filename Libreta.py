class Libreta:
    def __init__(self):
        self.libreta = []
    
    def guardar_contacto(self, contacto=None):
        self.libreta.append(contacto)