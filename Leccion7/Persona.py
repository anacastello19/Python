class Persona:#Esta clase gereda de la clase objet
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre= nombre

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad=edad

    def __str__(self): #Override= sobreescribir
         return f'Persona: [Nombre: {self._nombre}, Edad: {self._edad}'

class Empleado(Persona):#Esta clase es hija de la clase persona
        def __init__(self, nombre, edad, sueldo):
            super().__init__(nombre, edad)
            self.sueldo = sueldo
        @property
        def sueldo(self):
            return self._sueldo
        @sueldo.setter
        def sueldo(self, sueldo):
            self._sueldo=sueldo



#Tarea encapsular los atributos y crear setter and getter
#Cear otro objeto...
def __str__(self):
    return f'Empleado[Sueldo: {self._sueldo}'
empleado1=Empleado('Ariel', 40, 150000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

