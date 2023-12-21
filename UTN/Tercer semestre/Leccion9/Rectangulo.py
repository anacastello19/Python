from Color import Color
from FigurasGeometrica import FigurasGeometrica

class Rectangulo(FigurasGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FigurasGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto* self._ancho

    def __str__(self):
        return f'{FigurasGeometrica.__str__(self)} {Color.__str__(self)}'