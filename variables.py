# ejemplos de casting
a = 10 
b = 10.5
print(type(a))
print(type(b))

#ejemplos isinstance
print(isinstance(a,int))
print(isinstance(b,int))

#ejemplos de cambios de variables int() float() complet() str()
print(int(18.6))
print(float(12))
print(complex(6))
print(str(123568))

#ejemplos de que tipo son type()
print(type(123))
print(type(123.456))
print(type('hola'))

#redondear al numero mas cercano round()
print(round(12.456))
#nos devuelve el numero mayor
print(max(12.456,12.567))
#nos devuelve el numero menor
print(min(12.456,12.567))

#cadenas de texto
s = "hola" "que tal" "el" "dia"
print(s)
v = "muy bien"
print(s + v)
print("hola", "que tal", "el", "dia")

#multiplicar cadenas
print(s*3)

# cadena de caracteres
cadena = 'hola'
print(cadena[0])
print(cadena[1])
print(cadena[2])

#unir 2 cadenas de caracteres
cadena1 = 'hola'  
cadena2 = 'como'
cadena3 = 'estas'
print(cadena1 + cadena2 + cadena3)

#ejenplos de slicing
palabra = 'python'
print(palabra[0])
print(palabra[1])
print(palabra[-2])
print(palabra[0:2])
print(palabra[3:0])
print(palabra[:])

#end
print('hola', end=' ')
print('como', end=' ')
print('estas')