from Color import Color
from FigurasGeometrica import FigurasGeometrica


class Cuadrado(FigurasGeometrica, Color):
    def __init__(self, lado, color):
        #super.__init__(lado)
        FigurasGeometrica.__init__(self, lado, lado)
        Color.__init__(self,color)

    def calcular_area(self):
        return self.alto*self.ancho


    def __str__(self):
        return f'{FigurasGeometrica.__str__(self)} {Color.__str__(self)}'

