import csv
from os.path import join
from files.Files import *

opciones = "*********************\n1.- Agregar\n2.- Mostrar\n3.- Modificar\n4.- Eliminar\n5.- Salir\n*********************"

def Guardar(cedula, nombre, apellido, carrera):
 obA = Archivo()
 datos = cedula + ";" + nombre+ ";" +apellido+ ";" +carrera+ ";\n"
 obA.create("personas.csv", datos, "a")


def Mostrar():
   obA = Archivo()
   lista = obA.getStudets("personas.csv")
   for i in range(len(lista)):
       print(lista[i].getData())



while True:
 print(opciones)
 ops = int(input('Ingresar Transaccion: '))
 if ops == 1:
   print('Agregar')
   cedula = input('ingrese cedula: ')
   nombre = input('ingrese nombre: ')
   apellido = input('ingrese apellid: ')
   carrera = input('ingresar carrera: ')
   Guardar(cedula, nombre, apellido, carrera)

 elif ops == 2:
  print('Mostrar')
  Mostrar()
 elif ops == 3:
  print('Modificar')
  input('ingresar cedula: ')
  #Buscar(cedula)

 elif ops == 4:
  print('Eliminar')

 elif ops == 5:
  print('*********************\nGracias Por Usar Nuestro Servicio\n*********************')
  break
"""
obA = Archivo()
msg = "123456790;CARLA LUISA;PINELA MENDIETA;MEDICINA;\n"
#obA.create("personas.csv",msg,"a")


cedula = input("Cedula:")
lista= obA.getStudets("personas.csv")
pos = obA.getPosicion(cedula,lista)
if pos!=-1:
    #lista.pop(pos)
    nombre = input("Nombre:")
    apellido = input("Apellido:")
    carrera = input("Carrera:")
    lista[pos].nombre = nombre
    lista[pos].apellido = apellido
    lista[pos].carrera = carrera
    cad =""
    for i in range(len(lista)):
        cad = cad +lista[i].cedula+";"+ lista[i].nombre+";"+lista[i].apellido+";"+lista[i].carrera+";\n"
    obA.create("personas.csv",cad,"w")
    
for i in range(len(lista)):
    print(lista[i].getData())

"""


