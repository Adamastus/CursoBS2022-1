# son funciones que hacemos cuando no sabemos cuántos argumentos tendrá la función
# un asterisco significa que no sabemos la cantidad de argumentos
# el nombre args espor convencion, lo importante es el *

#hacer una funcion que calcule la media de unos valores que no sabemos cuantos son

def calcular_media(*args):
  total = 0
  for i in args:
    total += i
  resultado_media = total / len(args)
  return resultado_media

a,b,c = 5,15,10
media = calcular_media(a,b,c)

print (f"La media de los valores {a},{b},{c} es {media}")

  
