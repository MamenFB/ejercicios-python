#los conjuntos no son anidables
numeros = {1,2,3,4,5,6,7,8,9,10, "que tal"}
print(numeros)
print(type(numeros))

#añadir elementos .add()
numeros.add(11)
print(numeros)

#añadir elementos .update() pero donde caiga
numeros.update([12,13,14,15,16,17,18,19,20,21])
print(numeros)

#borrar elementos .remove()
numeros.remove(11)
print(numeros)

#borrar elementos .discard()
numeros.discard(5)
print(numeros)

#con el metodo in() buscamos
print(5 in numeros)
#con pop() sacamos el ultimo elemento
print(numeros.pop())
#clear() eliminamos
numeros.clear()
print(numeros)