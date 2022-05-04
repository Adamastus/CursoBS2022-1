# Ejemplo de función nula

def funcion_nula():
  print("Python")
  return

funcion_nula()



# Ejemplo función productiva

def funcion_productiva(a,b):
  print("Suma de a y b es => ", a+b)
  return

funcion_productiva(74,52)



# Ejemplo función normal y luego en formato lambda

def multiplicar(x,y):
  return x * y

print(multiplicar (5,5))

# en formato lambda

multiplicar = lambda x,y : x * y 
print(multiplicar(5,5))

# mismo ejemplo dentro de una expresión

print(f"{(lambda x : x * 6)(8)}")


  
