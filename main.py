import csv
from os.path import join
from files.Files import *

opciones = "*********************\n1.- Agregar\n2.- Mostrar\n3.- Modificar\n4.- Eliminar\n5.- Salir\n*********************"

def Guardar(cedula, nombre, apellido, carrera,cede):
 objetoArchivo = Archivo()
 datos = cedula + ";" + nombre+ ";" +apellido+ ";" +carrera+" "+cede+ ";\n"
 objetoArchivo.crear("personas.csv", datos, "a")


def Mostrar():
   objetoArchivo = Archivo()
   lista = objetoArchivo.obtenerEstudiantes("personas.csv")
   for i in range(len(lista)):
       print(lista[i].Datos())

def Actualizar():
    objetoArchivo = Archivo()
    cedula = input("Cedula:")
    lista = objetoArchivo.obtenerEstudiantes("personas.csv")
    pos = objetoArchivo.obtenerPosicion(cedula, lista)
    if pos != -1:
        nombre = input("Nombre:")
        apellido = input("Apellido:")
        carrera = input("Carrera:")
        cede = input("cede:")
        lista[pos].nombre = nombre
        lista[pos].apellido = apellido
        lista[pos].carrera = carrera
        lista[pos].cede = cede
        cad = ""
        for i in range(len(lista)):
            cad = cad + lista[i].cedula + ";" + lista[i].nombre + ";" + lista[i].apellido + ";" + lista[
                i].carrera +" "+ cede + ";\n"
        objetoArchivo.crear("personas.csv", cad, "w")

def Eliminar():
    objetoArchivo = Archivo()
    cedula = input("Cedula:")
    lista = objetoArchivo.obtenerEstudiantes("personas.csv")
    pos = objetoArchivo.obtenerPosicion(cedula, lista)
    if pos != -1:
        lista.pop(pos)
        cad = ""
        for i in range(len(lista)):
            cad = cad + lista[i].cedula + ";" + lista[i].nombre + ";" + lista[i].apellido + ";" + lista[
                i].carrera + ";\n"
        objetoArchivo.crear("personas.csv", cad, "w")


while True:
 print(opciones)
 ops = int(input('Ingresar Transaccion: '))
 if ops == 1:
   print('Agregar')
   cedula = input('ingrese cedula: ')
   nombre = input('ingrese nombres: ')
   apellido = input('ingrese apellidos: ')
   carrera = input('ingresar carrera: ')
   cede = input('ingresar cede: ')
   Guardar(cedula, nombre, apellido, carrera, cede)

 elif ops == 2:
  print('Mostrar')
  Mostrar()
 elif ops == 3:
  print('Modificar')
  #input('ingresar cedula: ')
  Actualizar()

 elif ops == 4:
  print('Eliminar')
  Eliminar()

 elif ops == 5:
  print('*********************\nGracias Por Usar Nuestro Servicio\n*********************')
  break



