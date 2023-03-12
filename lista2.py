from juegos import Plataformas

class ListaDoble2:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertarFinal(self, code):
        plata = Plataformas(code)
        if self.primero is None:
            self.primero = plata
            self.ultimo = plata
        else:
            plata.anterior = self.ultimo
            self.ultimo.siguiente = plata
            self.ultimo = plata

    def mostrar3(self):
        if self.primero is None:
            print("la lista vacia")
        else:
            aux = self.primero
            while aux is not None:
                print(aux.codigo)
                aux = aux.siguiente

    def insertarOrdenado(self, code):
        plata = Plataformas(code)
        if self.primero is None:
            self.primero = plata
            self.ultimo = plata
        else:
            if plata.codigo < self.primero.codigo:
                plata.siguiente = self.primero
                self.primero.anterior = plata
                self.primero = plata
            elif plata.codigo > self.ultimo.codigo:
                plata.anterior = self.ultimo
                self.ultimo.siguiente = plata
                self.ultimo = plata
            else:
                aux = self.primero
                while aux.codigo < plata.codigo:
                    aux = aux.siguiente
                plata.anterior = aux.anterior
                plata.siguiente = aux
                aux.anterior.siguiente = plata
                aux.anterior = plata
    
    def ordenarBurbuja(self):
        aux = self.primero
        while aux is not None:
            aux2 = aux.siguiente
            while aux2 is not None:
                if aux.codigo > aux2.codigo:
                    temp = aux.codigo
                    aux.codigo = aux2.codigo
                    aux2.codigo = temp
                aux2 = aux2.siguiente
            aux = aux.siguiente

    def escribirXMLPlataformas(self):
        if self.primero is None:
            print("La lista esta vacia")
        else:
            archivo = open("salidas.xml", "a")
            aux = self.primero
            while aux is not None:
                archivo.write("\n\t\t<Plataforma>\n")
                archivo.write("\t\t\t<codigo>" + aux.codigo + "</codigo>\n")
                archivo.write("\t\t</Plataforma>\n")
                aux = aux.siguiente
            archivo.close()