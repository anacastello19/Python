from Empleados import Empleados
from Gerente import Gerente


def imprimir_detalles(objeto):
    #print(objeto)  # De manera indirecta llama al str de la clase Empleado o Gerente
    print(type(objeto))  # Esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())
    print(objeto.departamento)
    #Polimorfismo

    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleados('Ariel', 55000)
imprimir_detalles(empleado)

gerente = Gerente('Natalia', 6000, 'Sistema')
imprimir_detalles(gerente)
