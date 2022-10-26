class Rectangulo:
    '''
    Crear la clase rectangulo, debe tener 2 atributos:
    altura, y base
    El nombre del metodo sera calcular el area utilizando
    la formula:
    area= base*altura.
    Pero la base y la altura deben ser ingresadas por el
    usuario y los objetos deben ser tres.
    '''
    print('Calculamos un Rectangulo')
    def __init__(self, base, altura):
        self.base= base
        self.altura= altura

    def area(self):
        return self.altura*self.base

base= int(input("Digite el la base: "))
altura= int(input('Digite el la altura: '))

rec= Rectangulo(altura, base)
print(f'El resultado del rectangulo es: {rec.area()}')

