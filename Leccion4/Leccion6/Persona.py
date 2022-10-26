class Persona: #Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #Se lo llama metodo Init Dunder
        self.nombre= nombre
        self.apellido= apellido
        self._dni=dni #Este atributo esta en capsulado de manera sugerida
        self.edad = edad
        self.args= args
        self.kwargs= kwargs

    def mostrar_detalle(self):
        print(f"La clase Persona tiene los siguientes datos: {self.nombre} {self.edad} {self.apellido}, la direccion es: {self.args}, los datos importan son: {self.kwargs}")

persona1 = Persona('Ariel', 'Betancurd',155641564415, 40)#Necesitamos enviat argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2= Persona('Osvaldo','Giordanini',45)
print(f'El objeto 2 de la clase persona: {persona2.nombre} {persona2.edad} su edad es: {persona2.edad}')

persona1.nombre='Liliana'
persona1.apellido='Bucella'
persona1.edad=40
print(f'El objeto 2 de la clase persona: {persona1.nombre} {persona1.edad} su edad es: {persona1.edad}')

#Los atributos son las caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()#La referencia
persona2.mostrar_detalle()

#persona.mostrar_detalle()# Debemos pasarle una referencia parael self o dara error
persona1.telefono='554551'
print(f'Este es el numero de telefono de {persona1.nombre} {persona1.telefono}')

#print(persona2.telefono)# el objeto persona2 no tiene este atributo, da erro
persona3= Persona('Rogelio','Romero', 454553,22,'Telefono','56645645','Calle Lopez',252,'Manzana')
persona3.mostrar_detalle()
#print(persona3._dni) #Es una mala practica

persona3
