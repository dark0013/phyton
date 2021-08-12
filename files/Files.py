from domain.Entities import *
class Archivo:

    def create(self,nombre,data,mode):
        archivo = open(nombre,mode)
        archivo.write(data)
        archivo.close()

    def getStudets(self,name):
        lista = []
        try:
            archivo = open(name,"r")
            for linea in archivo.readlines():
                tupla = linea.split(";")
                obj = Estudiante(tupla[0],tupla[1],tupla[2],tupla[3])
                lista.append(obj)
            archivo.close()
        except:
              pass
        return lista

    def getPosicion(self,cedula,lista):
        pos = -1
        for i in range(len(lista)):
            if cedula == lista[i].cedula:
                pos = i
                break
        return pos