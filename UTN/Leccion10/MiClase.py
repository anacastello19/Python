class MiClase:
    # Variable de clase, esta atributo dara casa objeto el mismo valor
    var_clase = 'Esta es una variable  de clase'  # La variable de instancia, da diferentes valores

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():#metodo estatico se asocia a la clase
        print(MiClase.var_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.var_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.var_clase)
        print(self.variable_instancia)


print(MiClase.var_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)

#Los objetos tambien pueden acceder a la variable de clase
print(miClase1.var_clase)
print(miClase1.variable_instancia)
miClase2= MiClase('Esta es otra prueba de cariable de instancia')
print(miClase2.variable_instancia)
print(miClase2.var_clase)

MiClase.var_clase2="Valor de variable de clase 2"
print(MiClase.var_clase2)
print(miClase1.var_clase2)
print(miClase2.var_clase2)

MiClase.metodo_estatico()

MiClase.metodo_clase()
miObjeto1=MiClase('Variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()