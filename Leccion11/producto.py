class Producto:
    contador_productos=0 #Variable de clase

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1 #Aumenyo para la variable clase
        self._id_producto= Producto.contador_productos #Asignamos desde la variable clase
        self._nombre = nombre
        self._precio = precio
#Metodo Setter and Getter
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre= nombre

    @property
    def precio(self):
         self._precio

    @precio.setter
    def precio(self, precio):
        self._precio= precio

#Sobre escribimos el metodo str
    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre {self._nombre}, Prrecio {self._precio}'
if __name__== '  main  ': #Solo sera visible, la prueba se ejecuta desde aqui
        producto1= Producto('Camisa',  100.00)
        print(producto1)
        producto2= Producto('Pantalon', 150.00)
        print(producto2)
