
#crear una lista de 5 valores

def crear_lista(n):
  lista = []
  for i in range(n):
    lista.append(i)
  return lista

print(crear_lista(5))

#funcion Hola va a crear una lista de los nombres que le diga y los imprime

def hola(lista):
  for nombre in lista:
    print("Buen dia",nombre)

hola(["Maria","Juan","Marta"])



