 # Se obtienen dos números

numero1 = int(input("Escribre un número"))
numero2 = int(input("Escribre otro número"))

# Se elige el número mayor

if numero1 > numero2:
  numero_mayor = numero1

else:
  numero1 < numero2
  numero_mayor = numero2

print("El numero mayor es => ",numero_mayor)

# ejemplo doble if anidado

password = input("Ingresa la clave: ")

if len(password) >= 8:
  print("Clave verificada.")
  
  if password == "12345678":
    print("Clave correcta.")
  else:
    print("Clave incorrecta.")

else:
  password != "12345678"
  print('Tu clave tiene menos de 8 caracteres o es incorrecta.')

