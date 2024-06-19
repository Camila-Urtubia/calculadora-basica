#Función para sumar: 
def suma(numero_1, numero_2):
  resultado = numero_1 + numero_2
  return resultado

# Función para restar:
def resta(numero_1, numero_2):
  resultado = numero_1 - numero_2
  return resultado

# Función para multiplicar:
def multiplicar(numero_1, numero_):
  resultado = numero_1 * numero_2
  return resultado

# Función para dividir:
def dividir(numero_1, numero_2):
  if numero_2 != 0:
    resultado = numero_1 / numero_2
    return resultado
  else:
    print("No se puede dividir por 0")

# Menú
while True:
 print("1. Sumar.")
 print("2. Restar.")
 print("3. Multiplicar.")
 print("4. Dividir.")
 print("5. Salir.")
 opcion = int(input("Ingrese el número de la operación que desea realizar: "))
 print()

 if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
   numero_1 = int(input("Ingrese un número: "))
   numero_2 = int(input("Ingrese un segundo número: "))
   print()

   if opcion == 1:
    print(f"El resultado de la suma es: {suma(numero_1, numero_2)}")
    print()

   elif opcion == 2:
    print(f"El resultado de la resta es: {resta(numero_1, numero_2)}")
    print()

   elif opcion == 3:
    print(f"El resultado de la múltiplicacion es: {multiplicar(numero_1, numero_2)}")
    print()

   elif opcion == 4:
    print(f"El resultado de la división es: {dividir(numero_1, numero_2)}")
    print()

 elif opcion == 5:
  print("Saliendo del programa.")
  break

 else:
  print("numero no válido")
  print()
  
