'''
PLANTEAMIENTO DEL PROBLEMA:

Calcula n! en base a los valores de n
La formula es: n!=(((2*pi)**0.5)*e**(-n))*(n**(n+1/2))'''

# PROBLEMA: calcular n!
# ENTRADAS: n
# SALIDA: n!
# ALGORITMO
# 1. Leer n
# 2. Calcular n! usando la formula dada
# 5. Mostrar n!  con 2 decimales

#Contrato de funciones 
#Leer Datos()
#Entrada: Ninguna
#Salida: n
#Responsabilidad: pedir datos al usuario

#Calcular_n!(n)
#Entrada: n
#Salida: n!
#Responsabilidad calcular el valor de n! de acuerdo a la formula dada
# n!=(((2*pi)**0.5)*e**(-n))*(n**(n+1/2) , no imprimir

#mostrar(n!)
#Entrada: n!
#Salida: ninguna
#Responsabilidad: mostrar el valor de n! con 2 decimales

#Casos de pruebas
# Caso 1:
# Entradas: 5
# Salida esperada: 118.019168


# Restricciones:
# - no imprimir dentro de la funcion
# - devolver el resultado
# - no usar bibliotecas externas
# - no usar variables globales
# - no realizar llamadas a funciones de este archivo

def leer_datos_2():
    n = int(input("Ingrese el valor de n: "))
    return n

def calcular_n(n):
    return (((2 * 3.1416) ** 0.5) * (2.7183 ** (-n))) * (n ** (n + 0.5))

def mostrar_resultado(resultado):
    print(f"El resultado es: {resultado:.2f}")
