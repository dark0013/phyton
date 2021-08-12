class Persona:

    def __init__(self,cedula,nombre,apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    def Datos(self):
        return self.cedula+" "+self.nombre+" "+self.apellido

class Estudiante(Persona):

    def __init__(self,cedula,nombre,apellido,carrera,cede):
        super().__init__(cedula,nombre,apellido)
        self.carrera = carrera
        self.cede = cede

    def Datos(self):
        return super().Datos()+" "+self.carrera+" "+self.cede