class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad= edad

    def __add__(self, other):#other significa otro
        return f'{self.nombre}, {other.nombre}'

    def __str__(self, otro):#sub significa subtraccion(resta)
        return self.edad-otro.edad



persona1= Persona('Ana', 50)
persona2= Persona('Arie', 40)

#persona1.__add__(persona2) sintaxis interna y automatica

print(persona1+persona2)
print(persona1-persona2)