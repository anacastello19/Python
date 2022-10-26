class Vehiculo:
    '''
    Definir una clase llamada Vehiculo y dos clases hijas
    llamadas Auto y Bici, las cuales heredan de la clase padre
    vehiculo. La clase padre debe tener los sig atributos y
    metodos:

    Vehiculo(Clase padre)
    *Atributo (color, rueda)
    *Metodos (__init__(color, ruedas) y __str__())

    Auto(clase hija de Vehiculo)
    *Atributos(Velocidad(km/hr))
    *Metodos (__init__(color, ruedas, velcidad) y __str__)

    Bicicleta(clase hija de vehiculo)
    *Atributos(tipo(urbana/montana/etc.))
    *Metodos(__init__(color, ruedas, tipos) y __str__())

    Crear un objetos de cada clase
    '''

class Vehiculo:
    def __init__(self, rueda, color):
        self.rueda= rueda
        self.color= color


    def __str__(self):
        return 'Rueda: '+ str(self.rueda)+', color: '+ self.color


class Bicicleta(Vehiculo):
        def __init__(self, rueda, color, tipos):
            super().__init__(rueda,color)
            self.tipos = tipos

        def __str__(self):
            return f'El tipo de bicicleta es: {self.tipos}, {super().__str__()}'

class Auto(Vehiculo):
        def __init__(self,rueda, color, velocidad):
            super().__init__(rueda, color)
            self.velocidad = velocidad

        def __str__(self):
            return super().__str__()+', Velocidad: '+ str(self.velocidad)+'km/hs'

#Primer Objeto
vehiculo= Vehiculo(29,'Rojo')
print(vehiculo)
#Sgundo Objeto
auto=Auto (29,'blanco',100)
print(auto)
#tercer objeto
bicicleta= Bicicleta(26,'Azul y negro',', Urbana')
print(bicicleta)