'''
PLANTEAMIENTO DEL PROBLEMA:

Calcula el salario semanal de 
un trabajador. Las horas 
mayores a 40 se pagan al 
triple'''

# PROBLEMA: calcular salario semanal
# ENTRADAS: horas_trabajadas, pago_por_hora
# SALIDA: salario_semanal
# ALGORITMO
# 1. Leer horas trabajadas
# 2. Leer pago por hora
# 3. Si horas <= 40:
#       salario = horas * pago
# 4. Si no:
#       extra = horas - 40
#       salario = (40 * pago) + (extra * pago * 2)
# 5. Mostrar salario con 2 decimales

#Contrato de funciones 
#Leer Datos()
#Entrada: ninguna
#Salida: horas y pago
#Responsabilidad: pedir datos al usuario

#Calcular Salario(horas, pago)
#Entrada: horas, pago
#Salida: salario
#Responsabilidad calcular, no imprimir

#mostrarSalario(salario)
#Entrada: salario
#Salida: ninguna
#Responsabilidad: mostrar resultado

#Casos de pruebas
# Caso 1:
# Entradas: 40, 10
# Salida esperada: 400
# Caso 2:
# Entradas: 45, 10
# Salida esperada: 475
# Caso 3:
# Entradas: 50, 20
# Salida esperada: 1200

# Restricciones:
# - no imprimir dentro de la funcion
# - devolver el resultado
# - no usar bibliotecas externas
# - no usar variables globales
# - no realizar llamadas a funciones de este archivo

def leer_datos():
    horas = float(input("Ingrese las horas trabajadas: "))
    pago = float(input("Ingrese el pago por hora: "))
    return horas, pago

def calcular_salario(horas, pago):
    if horas <= 40:
        salario = horas * pago
    else:
        extra = horas - 40
        salario = (40 * pago) + (extra * pago * 3)
    return salario

def mostrar_salario(salario):
    print(f"El salario semanal es: {salario:.2f}")
     