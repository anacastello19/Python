class Cubo:
    '''
    Crea una clase llamada Cubo con los atrinutos, ancho, alto y produndidad,
    con un metodo calcular_volumen que tendra la formula:
    volumen = ancho*altura * profundidad
    que el usuario ingrese lo valores.

    '''
    print('Calculemos el volumen del cubo!')

    def __init__(self, ancho, altura, profundidad):
        self.ancho= ancho
        self.altura= altura
        self.profundidad = profundidad

    def volumen(self):
        return self.ancho* self.altura* self.profundidad

ancho= int(input('Digite el ancho del cubo: '))
altura= int(input('Digite el altura el cubo: '))
profundida= int(input('Digite la profundidad del cubo: '))

cubo1= Cubo(ancho, altura, profundida)
print(f'El volumen del cubo es: {cubo1.volumen()}')
