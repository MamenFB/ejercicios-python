# definir una funcion max() que tome 2 numeros como argumentos y devuelva el mayor
def funcion_max(a,b):
    if a > b:
        return a
    else:
        return b
print(funcion_max(560,-8956))

# tome 3 numeros y devuelva el mayor de los 3
def funcion_max_3(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(funcion_max_3(560,-8956,1000))

# numero que toma por caracter una vocal
def is_vocal(caracter):
    vocal = ['a','e','i','o','u']
    if caracter in vocal:
        return True
    else:
        return False
print(is_vocal('a'))

# imprimir una escalera ascendente
if __name__ == "__main__":
    n = int(input('Ingrese el numero de filas: '))
    for i in range(1, n+1):
        print(''* (n-i) + '#' * i)

  # imprimir una escalera descendente
if __name__ == "__main__":
  n = int(input(' numero de filas: '))
  for i in range(n, 0, -1):
      print(''* (n-i) + '#' * i)

