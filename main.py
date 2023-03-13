from listad import ListaDoble
from lista1 import ListaDoble1
from lista2 import ListaDoble2
import xml.etree.ElementTree as ET

if __name__ == '__main__':

    print(" ")
    direccion = input("Ingrese la ruta del archivo: \n")
    tree = ET.parse(direccion)
    
    root = tree.getroot()

    lista = ListaDoble()
    lista1 = ListaDoble1()
    lista2 = ListaDoble2()
    
    for ADIOS in root.findall('ListaPlataformas'):
        for AMOR in ADIOS.findall('Plataforma'):
            codigo = AMOR.find('codigo').text
            nombre = AMOR.find('nombre').text
            lista.insertarOrdenado(codigo, nombre)
    lista.escribirXML()

    for DE in root.findall('ListadoJuegos'):
        lista1 = ListaDoble1()
        for LOS in DE.findall('Juego'):
            codigo = LOS.find('codigo').text
            nombre = LOS.find('nombre').text
            #lista2.insertarOrdenado(LOS)
            lista1.insertarOrdenado(codigo, nombre)
            for BESOS in LOS.findall('Plataformas'):
                lista2 = ListaDoble2()
                for QUE in BESOS.findall('Plataforma'):
                    DI = QUE.find('codigo').text
                    lista2.insertarOrdenado(DI)
                    #lista1.insertarOrdenado(codigo, nombre)
                lista1.escribirXML(lista2)
                


    #lista1.ordenarBurbuja1()
    print("-----------------")
    lista.mostrar()
    lista1.mostrar1()
    lista2.mostrar3()
    print("-----------------")
    #lista.escribirXML()
    

