class Persona:
    # pass #No se procesa nada mas
    def __init__(self, nombre, apellido, edad):  # Metodo, self parametro por default y significa uno mismo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# Creamos un objeto y sus referencia
# indicamos que persona1 es un objeto de la clase y enviamos argumentos
persona1 = Persona('Ana', 'Castello', 24)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

p2=Persona('Javier', 'Perez', 44)
print(f"{p2.nombre} {p2.apellido} tiene {p2.edad} años")