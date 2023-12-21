'''
#Calcular estacion del año con if/elif/else
#Pedir al usuario que ingrese un mes del año el valor debe ser entre 1 y 12
#luego decimos en que estacion se encuentra

mes=int(input("Ingrese el numero de mes: "))

if mes==1 or mes==2 or mes==3:
    print("Este mes es verano")
elif mes==4 or mes ==5 or mes==6:
    print("Este mes es otoño")
    
elif mes==7 or mes==8 or mes ==9:
    print("Este mes es invierno")
    
elif mes==10 or mes==11 or mes==12:
    print('Este mes es primavera!')
    
else:
    print("Error, el mes no esta dentro del rango permitido (de 1 a 12)")
    
'''

'''
listas
'''
frutas=['manzana', 'pera', ' banana']
for fruta in frutas:
    print(fruta)
    
#Cuantos elementos tiene la lista?
print(len(frutas))
#Agregamos un elemento a la lista
frutas.append('frutilla')
#Insertamos un elemento donde deseemos que este
frutas.insert(1,'naranja')
