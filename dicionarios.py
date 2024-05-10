vehiculos = {
  'carro':10,
  'moto':5,
  'camion':8
  }  
print(vehiculos)

#metodo get() 
print(vehiculos.get('carro'))

#asignacion
vehiculos['carro'] = 12
print(vehiculos)

#agregar
vehiculos['bici'] = "roja"
print(vehiculos)

#borrar el ultimo popitem()
vehiculos.popitem()
print(vehiculos)

#hacer copia .copy()
vehiculosCopia = vehiculos.copy() 
print(vehiculosCopia)

#sum()

