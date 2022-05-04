#Para verificar más de una condición se utiliza elif, que se detiene en la primera sentencia verdadera.
# Se obtienen dos números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Se elige el número mayor

if numero1 == numero2:
  print("Los números tienen idéntico valor")
elif numero1 > numero2:
  numero_mayor = numero1
else:
  numero_mayor = numero2

print("El número mayor es:", numero_mayor)

#else no es obligatorio.
#Si no hay un else en la cascada, puede que no se ejecute ninguna de las opciones disponibles.
# else siempre es la última sentencia.
# Siempre le debe preceder un if.

x = 100
y = 500

if y > x:
  print(y, '(y) es mayor que', x, ('x'))
elif x == y:
  print(x, '(x) e (y)', y, 'tienen el mismo valor')
else:
  print(x, '(x) es mayor que', y, ('y'))
