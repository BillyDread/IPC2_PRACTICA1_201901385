from juegos import Plataforma

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertarFinal(self, code, name):
        plata = Plataforma(code, name)
        if self.primero is None:
            self.primero = plata
            self.ultimo = plata
        else:
            plata.anterior = self.ultimo
            self.ultimo.siguiente = plata
            self.ultimo = plata

    def mostrar(self):
        if self.primero is None:
            print("la lista vacia")
        else:
            aux = self.primero
            while aux is not None:
                print(aux.codigo, aux.nombre)
                aux = aux.siguiente

    def insertarOrdenado(self, code, name):
        plata = Plataforma(code, name)
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
                    temp = aux.nombre
                    aux.nombre = aux2.nombre
                    aux2.nombre = temp

                    temp = aux.codigo
                    aux.codigo = aux2.codigo
                    aux2.codigo = temp
                aux2 = aux2.siguiente
            aux = aux.siguiente

    def escribirXML(self):
        if self.primero is None:
            print("La lista esta vacia")
        else:
            archivo = open("externo.xml", "w")
            archivo.write("<JuegosViejos>\n")
            archivo.write("\t<ListaPlataformas>\n")

            aux = self.primero
            while aux is not None:
                archivo.write("\t\t<Plataforma>\n")
                archivo.write("\t\t\t<codigo>" + aux.codigo + "</codigo>\n")
                archivo.write("\t\t\t<nombre>" + aux.nombre + "</nombre>\n")
                archivo.write("\t\t</Plataforma>\n")
                aux = aux.siguiente
            archivo.write("\t</ListaPlataformas>")
            archivo.close()