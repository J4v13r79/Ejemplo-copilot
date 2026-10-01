'''
PLANTEAMIENTO DEL PROBLEMA:

Calcula x en base a los valores de a, b y c
La formula es: x = raiz de (b-a^2)**0.5/c'''

# PROBLEMA: calcular x
# ENTRADAS: a, b, c
# SALIDA: x
# ALGORITMO
# 1. Leer a
# 2. Leer b
# 3. Leer c
# 4. calcular x = raiz de (b-a^2)**0.5/c
# 5. Mostrar x con 2 decimales

#Contrato de funciones 
#Leer Datos()
#Entrada: Ninguna
#Salida: a, b, c
#Responsabilidad: pedir datos al usuario

#Calcular x
#Entrada: a, b, c
#Salida: x
#Responsabilidad calcular el valor de x de acuerdo a la formula dada, no imprimir

#mostrarX(x)
#Entrada: x
#Salida: ninguna
#Responsabilidad: mostrar el valor de x con 2 decimales

#Casos de pruebas
# Caso 1:
# Entradas: 2, 20, 5 
# Salida esperada: 0.8


# Restricciones:
# - no imprimir dentro de la funcion
# - devolver el resultado
# - no usar bibliotecas externas
# - no usar variables globales
# - no realizar llamadas a funciones de este archivo

def leer_datos_1():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    return a, b, c

def calcular_x(a, b, c):
    if c == 0:
        return None
    return (b - a**2)** 0.5 / c

def mostrar_x(x):
    if x is not None:
        print(f"El valor de x es: {x:.2f}")
    else:
        print("No se puede calcular x.")
