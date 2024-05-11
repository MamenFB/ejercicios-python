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


#variable self
class Galleta:
    def __init__(self, sabor, forma):
        self.sabor = sabor
        self.forma = forma
        
        print('se acaba de crear una galleta {}, y {}'.format(self.sabor, self.forma))

galleta1 = Galleta('chocolate', 'cuadrada')
galleta2 = Galleta('limon', 'cuadrada')

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

        print('se acaba de crear una mascota {}, de {} años y de raza {}'.format(self.nombre, self.edad, self.raza))

Mascota1 = Mascota('toby', 10, 'perro')
Mascota2 = Mascota('daysi', 2, 'gato')
Mascota3 = Mascota('snupy', 6, 'periquito')
Mascota4 = Mascota('Firulais', 10, 'perro')

class Galleta():
    chocolate = False

    def __init__(self):
        print('se acaba de crear una galleta')

    def chocolatera(self):
        self.chocolate = True
        
    def tieneChocolate(self):
        if self.chocolate:
            print('tiene chocolate')
        else:
            print('no tiene chocolate')

galleta1 = Galleta()
galleta1.chocolatera()
galleta1.tieneChocolate()

#chocolate es un atributo de clase
#self.chocolate es un atributo de instancia
#diferencias entre atributos de clase y atributos de instancia:
#atributo de clase es el mismo para todas las instancias de la clase 
#atributo de instancia es diferente para cada instancia de la clase

#metodo __init__ es el constructor de la clase
#metodo __str__ es el metodo que devuelve una cadena de texto cuando se imprime una instancia de la clase
#metodo __del__ es el metodo que se ejecuta cuando se elimina una instancia de la clase

#__atributo privado__ inalcanzable desde fuera de la clase
#getter y setter son: metodos que permiten acceder a un atributo privado desde fuera de la clase
#getter: devuelve el valor de un atributo privado
#setter: modifica el valor de un atributo privado
class Ejemplo:
    __atributoPrivado = "soy un atributo privado"
    def __metodo_privado(self):
        print("soy un metodo privado")
    def metodo_publico(self):
        print("soy un metodo publico")
    
    @property
    def atributo_publico(self):
        print("soy un getter")
        return self.__atributoPrivado


    @atributo_publico.setter
    def atributo_publico(self, valor):
        print("soy un setter")
        self.__atributoPrivado = valor
e = Ejemplo()

print(e.atributoPrivado)
e.atributoPrivado = "soy un nuevo valor"
print(e.atributoPrivado)
