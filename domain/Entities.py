class Persona:

    def __init__(self,cedula,nombre,apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    def getData(self):
        return self.cedula+" "+self.nombre+" "+self.apellido

class Estudiante(Persona):

    def __init__(self,cedula,nombre,apellido,carrera):
        super().__init__(cedula,nombre,apellido)
        self.carrera = carrera

    def getData(self):
        return super().getData()+" "+self.carrera