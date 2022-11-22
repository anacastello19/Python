class Persona:
    contador_persona = 0 #variable de clase

    @classmethod
    def gemerar_sig_valoe(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        self.id_pesona =Persona.contador_persona
        self.nombre= nombre
        self.edad= edad

    def __str__(self):
        return f'Persona [{self.id_pesona}= {self.nombre} {self.edad}]'

persona1= Persona('Ariel', 40)
print(persona1)
persona2= Persona('Osvaldo', 45)
print(persona2)
persona3= Persona('Liliana', 40)
print(persona3)
Persona.gemerar_sig_valoe()
persona4= Persona('Natalia', 35)
print(persona4)
print(f'Valor contador Persona: {Persona.contador_persona}')
