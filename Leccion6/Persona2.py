class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre=nombre
        self._apellido=apellido
        self._edad= edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre}, {self._apellido}, {self._edad}')

    @property#Decorar
    def nombre(self):#Metodo Getter
        print('Usando metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): #Metodo Setter
        print('Estamos usando metodo set')
        self._nombre= nombre

    @property
    def apellido(self, apellido):
        self._apellido= apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido= apellido

    @property
    def edad(self,edad):
        self._edad=edad

    @edad.setter
    def edad(self, edad):
        self._edad=edad


if __name__ != '__main__':
    pass
else:
    persona1 =Persona2('Ana', 'Fernandez', 30)
    print(persona1.nombre)#Llamamos al metodo getter
    persona1.nombre= 'Juan Pedro' #Lllamamos al metodo setter
    print(persona1.nombre)#Otra vez con el metodo getter
    print((persona1.mostrar_detalle()))#Llamamos el metodo mostrar_detalle
#Atributo read-only (solo lectura) seria
#print(persona1.edad)
#print(persona1.mostrar_detalle())

#Tarea crear tres objetos mas, utilizando los metodos getter and settet
#para modificar, y mostrar los cambios con el metodos ..

    persona3= Persona2('Julia','Castello', 25)
    persona3.nombre= 'Juli'
    persona3.apellido='Previde'
    persona3.edad=26
    print(persona3.mostrar_detalle())
    persona4=Persona2('Fanny','Castello',61)
    persona4.apellido='Previde'
    print(persona4.mostrar_detalle())

print(__name__)
