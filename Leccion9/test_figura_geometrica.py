from Cuadrado import Cuadrado
from FigurasGeometrica import FigurasGeometrica
from Rectangulo import Rectangulo

print('Creacion de onjetos clase Cuadrado'.center(50,'_'))
cuadrado1=Cuadrado(8,"Azul")
cuadrado1.alto=7
cuadrado1.ancho=7
#print(cuadrado1.ancho)
#print(cuadrado1.alto)
print(f'Calculo del area de cuadrado: {cuadrado1.calcular_area()}')

#MRO= Method Resolution Order
#print(Cuadrado.mro())

print(cuadrado1)

print('Creacion de objetos clases Rectangulo'.center(50,'_'))
rectangulo1= Rectangulo(3, 9,'verde')
rectangulo1.ancho=8
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)
#figura1= FigurasGeometrica() No se puede instancior

