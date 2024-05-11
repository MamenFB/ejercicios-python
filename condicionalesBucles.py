# if= si, else= si no, elif =sino si, while =mientras, for= para, break =salir, 
# continue continuar, pass =pasar, range(n) =n veces, len(lista) =longitud, sorted(lista) ordenar, 
# sum(lista) =sumar, min(lista) =minimo, max(lista) =maximo, list(conjunto)= lista,
# set(lista)= conjunto, tuple(lista)= tupla, dict(lista)= diccionario, zip(lista1,lista2) =zipear, 
# enumerate(lista) =enumerar, filter(funcion,lista)= filtrar, map(funcion,lista) =mapear, sorted( lista,key=funcion) 
# ordenar por funcion, reversed(lista) =invertir, del(lista)= borrar, del(diccionario) =borrar, del(tupla) 
# borrar, del(variable) borrar, del(funcion) borrar, del(clase) borrar, del(instancia) borrar, del(mod

#do while en python no existe, solo hay while
#la funcion range(n) es un generador, no es una lista, es mas eficiente
#la funcion sorted(lista) ordena la lista, key=funcion ordena la lista por funcion
#la funcion sum(lista) suma los elementos de la lista
#la funcion min(lista) devuelve el minimo de la lista
#la funcion max(lista) devuelve el maximo de la lista
#la funcion list(conjunto) devuelve una lista de los elementos del conjunto
#la funcion set(lista) devuelve un conjunto de los elementos de la lista
#la funcion tuple(lista) devuelve una tupla de los elementos de la lista
#la funcion dict(lista) devuelve un diccionario de los elementos de la lista
#la funcion zip(lista1,lista2) devuelve un zipeo de los elementos de las listas
#la funcion enumerate(lista) devuelve una tupla de la posicion y el elemento de la lista
#la funcion filter(funcion,lista) devuelve una lista con los elementos de la lista que cumplen la funcion
#la funcion map(funcion,lista) devuelve una lista con los elementos de la lista que pasan por la funcion
#la funcion sorted( lista,key=funcion) ordena la lista por funcion
#la funcion reversed(lista) devuelve una lista invertida
#la funcion del(lista) borra la lista
#la funcion del(diccionario) borra el diccionario
#la funcion del(tupla) borra la tupla
#la funcion del(variable) borra la variable
#la funcion del(funcion) borra la funcion
#la funcion del(clase) borra la clase
#la funcion del(instancia) borra la instancia
#la funcion del(mod) borra el modulo
#la funcion del(metodo) borra el metodo
#la funcion del(atributo) borra el atributo
#la funcion del(propiedad) borra la propiedad
#la funcion del(subclase) borra la subclase
#iteracion(es realizar una accion varias veces) en python es por indice, no por valor, por eso no se puede usar el for para recorrer diccionarios
#la funcion in(elemento,lista) devuelve true si el elemento esta en la lista
#white se rompe con break, si se rompe con continue, si no se rompe con pass
#bucle infinito while True

for i in range(10):
     print(i)

# enumerate 2 variables, la primera es la posicion y la segunda el elemento de la lista (indice y valor)
numeros = [1,2,3,4,5,6,7,8,9,10]
for indice, valor in enumerate(numeros):
    print(indice, valor)

#las cadenas son inmutables, no se pueden modificar
cadena = "hola amigos"
for letra in cadena:
    print(letra)
  
#ejemplo bucle for infinito
from itertools import count
contador =0
for i in count(): 
    print("interacion: ", contador )
    contador +=1
    if contador == 10:
        break
    