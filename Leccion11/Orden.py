from producto import Producto


class Orden:
    contador_ordenes= 0

    def __init__(self, productos):
        Orden.contador_ordenes+= 7
        self.id_orden= Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)#Esto es para agragar un nuevo producto

    def calcular_total(self):
        total=0 #Variable temporal para almecenar el total temporal
        for producto in self._productos:
            total += producto.precio
        return total
    def __str__(self):
        productos_str=''
        for producto in self._productos:
            productos_str+= producto.__str__()+'|'
        return f'Orden: {self.id_orden}, \nProductos: {productos_str}'
if __name__== '__main': #Solo sera visible
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    producto1 = [producto1, producto2]  # Lista de productos
    orden1 = Orden(producto1)  # Primer objeto orden pasando la lista de productos
    print(orden1)
