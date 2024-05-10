numero = [1,2,3,4,5,6,7,8,9,10]
print(numero)

datos = [1,2,3,4, "una cadena", 8,9,10]
print(datos)
print(type(datos))
print(len(datos))
print(datos[0])
print(len(numero))

#modificar
numero = [1,2,3,4,5,6,7,8,9,10]
numero[5] = 100
print(numero)

#append() 
numero = [1,2,3,4,5,6,7,8,9,10]
numero.append(108)
print(numero)

#insert()en la posicion 8 pone 50
numero.insert(8,50)
print(numero)

#borrar
numero[:2] = []
print(numero)

#buscar in
print(5 in numero)

#anidadas
lista = [1,2,3,4]
lista2 = [5,6,7,8]
lista3 = [9,10,lista,lista2]
print(lista3)

print(lista3[3][1])

#voltear cadena
cadena = "aloh nemam, 4321"
cadena2 = cadena[::-1]
print(cadena2)