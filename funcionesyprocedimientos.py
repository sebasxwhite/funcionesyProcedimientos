# -*- coding: utf-8 -*-
"""FuncionesYProcedimientos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UX6EZZQ7YnLAn13R8rW1mw7Qu_1DOxsA

##Función

Es un bloque que realiza una tarea especifíca y devuelve (return) un resultado.
Se utilizan en tareas repetitivas.

##Procedimiento

Es similar a una función NO devuelve un valor.

##Ventajas:

Permiten usar el mismo codigo una y otra vez. Hace que se divida el programa en partes más manejables y entendibles.
"""

def sumaDosNumeros(num1,num2):
  return num1 + num2

#Llamada a la función
print("La suma de los dos números es: ", sumaDosNumeros(5,7)) #En este caso nosotros le asignamos los números que queremos sumar.

#Pedirle el número al usuario
numero1=int(input("Ingrese el primero número: "))
numero2=int(input("Ingrese el segundo número: "))

print(f"La suma de los números {numero1} y {numero2} es: ", sumaDosNumeros(numero1,numero2))

def saludar(nombre):
  print("Hola", nombre, "bienvenido a tu página.")
saludar("Sebastián")

#Mini Calculadora

def suma(num1,num2):
  return num1 + num2
def resta(num1,num2):
  return num1 - num2
def multiplicar(num1,num2):
  return num1 * num2
def dividir(num1,num2):
  if num2!=0:
    return num1 / num2
  else:
    print("No se puede dividir por 0.")

#Pedir número al usuario

num1=float(input("Ingresa el primer número: "))
num2=float(input("Ingresa el segundo número: "))
operacion=input("Ingrese la operación que desea realizar: +,-,*,/")

if operacion=="+":
  print(f"El resultado de la suma de {num1} y {num2} es: ", suma(num1,num2))
elif operacion=="-":
  print(f"El resultado de la resta de {num1} y {num2} es: ", resta(num1,num2))
elif operacion=="*":
  print(f"El resultado de la multiplicación de {num1} y {num2} es: ", multiplicar(num1,num2))
elif operacion=="/":
  print(f"El resultado de la división de {num1} y {num2} es: ", dividir(num1,num2))

#Es par o impar

def imparPar(num1):
  if num1%2==0:
    return True
  else:
    return False
numUsuario=int(input("Ingrese el número: "))

if imparPar(numUsuario):
  print(f"El número {numUsuario} es par.")
else:
  print(f"El número {numUsuario} es impar.")

#Positivo o negativo

def posONeg(numero):
  if numero>0:
    return "Positivo"
  elif numero<0:
    return "Negativo"
  else:
    return "Neutro"

num=int(input("Ingrese un número: "))
print("El número que ingresaste es: ", posONeg(num))

#Tabla de multiplicación

def tablaMulti(numero):
  for i in range(1,13):
    print(f"{numero} x {i} = {numero * i}")

num=int(input("Ingrese el número al que le desea ver su tabla de multiplicacion: "))
print(tablaMulti(num))

#Suma de los números entre 1 a 'n'

def sumaHasta(num):
  suma=0 #Lugar donde se va a guardar la suma
  i=1 #Contador

  while i<=num:
    suma=suma+i
    i=i+1 # suma+=i
  return suma

n=int(input("Ingrese un número: "))
print(f"La suma de los números entre 1 y {n} es {sumaHasta(n)}")

#UN BUCLE QUE LE PIDA UN NUMERO INFINITAS VECES Y QUE SOLO SE DETENGA CUANDO SEA NEGATIVO

def numeroVar(num):
  if n>=0:
    return True
  else:
    print("Ingresaste un número negativo, fin del bucle")
    return False

n=int(input("Ingrese otro número: "))

while numeroVar(n):
  n=int(input("Ingrese otro número: "))

def pedirNumero():
  while True:
    numero=int(input("Ingresa un número (Negativo para detenerse)"))
    if numero<0:
      print("Se terminó el programa")
      break

pedirNumero()

numeros=[1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
  print(f"Revisando la lista de números, vamos en el numero {numero}")
  if numero==7:
    print("Número encontrado")
    break
  else:
    print("numero no encontrado")

nombres=["juan","juanjo","pedro","sebas","jose"]

nombreABuscar=input("Ingrese el número que deseas buscar: ")
for nombre in nombres:
  print(f"Revisando la lista de asistentes, estamos con {nombre}")
  if nombre==nombreABuscar:
    print(f"Nombre encontrado")
    break