class Aritmetica:
    """El nombre de esta tipo de comentario es:
    DocString
    Esto es la documentacion de la clase en python
    Vamos hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y mas

    """
    def __init__(self, operadorA, operadorB):
        self.operadorA= operadorA
        self.operadorB= operadorB

    #Metofo para sumar
    def sumar(self):
        return self.operadorA+ self.operadorB
    def restar(self):
        return self.operadorB-self.operadorA
    def multiplicar(self):
        return self.operadorB*self.operadorA
    def dividir(self):
        return self.operadorB/self.operadorA

aritmetica=  Aritmetica(7,9) # Lepasamos los argumentos para los operandos
print(f'La suma de los numero es {aritmetica.sumar()}')
print(f'La resta de los numeros es { aritmetica.restar()}')
print(f'La multiplicacion de los numeros es {  aritmetica.multiplicar()}')
print(f'La division de los numeros es { aritmetica.dividir()}')