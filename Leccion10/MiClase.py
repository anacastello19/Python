class MiClase:
    # Variable de clase, esta atributo dara casa objeto el mismo valor
    var_clase = 'Esta es una var de clase'  # La variable de instancia, da diferentes valores

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


print(MiClase.var_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)

#Los objetos tambien pueden acceder a la variable de clase
print(miClase1.var_clase)
print(miClase1.variable_instancia)
miClase2= MiClase('Esta es otra prueba de cariable de instancia')
print(miClase2.variable_instancia)
print(miClase2.var_clase)