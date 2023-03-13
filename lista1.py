from juegos import Juego

class ListaDoble1:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertarFinal(self, code, name):
        game = Juego(code, name)
        if self.primero is None:
            self.primero = game
            self.ultimo = game
        else:
            game.anterior = self.ultimo
            self.ultimo.siguiente = game
            self.ultimo = game

    def mostrar1(self):
        if self.primero is None:
            print("la lista vacia")
        else:
            aux = self.primero
            while aux is not None:
                print(aux.codigo, aux.nombre)
                aux = aux.siguiente

    def insertarOrdenado(self, code, name):
        game = Juego(code, name)
        if self.primero is None:
            self.primero = game
            self.ultimo = game
        else:
            if game.codigo < self.primero.codigo:
                game.siguiente = self.primero
                self.primero.anterior = game
                self.primero = game
            elif game.codigo > self.ultimo.codigo:
                game.anterior = self.ultimo
                self.ultimo.siguiente = game
                self.ultimo = game
            else:
                aux = self.primero
                while aux.codigo < game.codigo:
                    aux = aux.siguiente
                game.anterior = aux.anterior
                game.siguiente = aux
                aux.anterior.siguiente = game
                aux.anterior = game

    def ordenarBurbuja1(self):
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

    def escribirXML(self, listado):
        if self.primero is None:
            print("La lista esta vacia")
        else:
            archivo = open("externo.xml", "a")
            archivo.write("\n\t<ListadoJuegos>\n")

            aux = self.primero
            while aux is not None:
                archivo.write("\t\t<Juego>\n")
                archivo.write("\t\t\t<codigo>" + aux.codigo + "</codigo>\n")
                archivo.write("\t\t\t<nombre>" + aux.nombre + "</nombre>\n")
                archivo.write("\t\t\t<Plataformas>\n")
                archivo.close()
                listado.escribirXMLPlataformas()
                archivo = open("salidas.xml", "a")
                archivo.write("\t\t\t</Plataformas>\n")
                archivo.write("\t\t</Juego>\n")
                aux = aux.siguiente
            archivo.write("\t<ListadoJuegos>\n")
            archivo.write("</JuegosViejos>")
            archivo.close()