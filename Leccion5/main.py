# comenzamos con funciones
#definimos una funcion
def mi_funcion():
    print("Saludos a todeeesssss")
    print(("Kuak Kuak"))
mi_funcion() #llamo funcion para que apresca
mi_funcion()#Se puede llamar las veces que queramos

#Desempaquetado de lista o list Unpacking
def show(name, lastName):
    print(name+ ''+lastName)
person =['Ana ', ' Castello']
show(person[0], person[1]) #PASAMOS UNO POR UNO los datos de la lista
show(*person) #Esto es lo mismo que lo anterior
person2=('Virginia', 'Castello')
show(*person2)
person3={'lastName':'Ana', 'name':'Virginia'}
show(**person3)

numbers= [1,2,3,4,5,]
for n in numbers:
    print(n)
#Unica manera para que no se muestre el else
#If n==3:
#Break
else:
    print('Esto se termino')

#List comprehension, lista de comprension
name= ['Paolo','Rodrigo','Lupe','Pepe']
alsongP=[p for p in name if p[0]=='P'] #Esto regresa una nueva
print(alsongP)

bottleC=[{'name':'Quilmes','country':'Arg'},
         {'name':'Corona','country':'Mx'},
         {'name':'Stella Artois','country':'Belgium'},
         ]
Arg= [b for b in bottleC if b['country']=='Arg']
print(Arg)
print(bottleC)

#Paso de Argumentos (funciones)
def mi_funcion2(name, lastname):
    print('Saludos')
    print(f'Nombre: {name}, Apellido: {lastname}')
mi_funcion2('Ana','Castello')
mi_funcion2('Virginia', 'Previde')
mi_funcion2('Alguien', 'Loco')

#La palabras return en funciones
#Creamos una funcion para sumar
def sumar(a, b):
    return a+b
resultado = sumar(77,22)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55,45)}')

def sumar2(a=0, b=0): #Le damos un valor por default
    return a+b
resultado= sumar2()
print(f'Resulta de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22.66)}')

#Argumentos, variables en funciones
def listarNombres(*nombres): #Normalmente se utiliza *args
    for nombre in nombres: #Se va a convertir en una tupla
        print(nombre)
listarNombres('Ana', 'Mauro', 'Jaqueline', 'Valentina')
listarNombres('Cami','Nacho','Cintia')
