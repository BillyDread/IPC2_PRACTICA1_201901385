class Plataforma:
    def __init__(self, code, name):
        self.codigo = code
        self.nombre = name
        
        self.siguiente = None
        self.anterior = None

class Plataformas:
    def __init__(self, code):
        self.codigo = code
        
        self.siguiente = None
        self.anterior = None

class Juego:
    def __init__(self, code, name):
        self.codigo = code
        self.nombre = name

        self.siguiente = None
        self.anterior = None