from Soluciones.Salario_semanal import calcular_salario, mostrar_salario, leer_datos
from Soluciones.Ejercicio1 import calcular_x, mostrar_x,leer_datos_1
from Soluciones.Ejercicio2 import calcular_n, mostrar_resultado, leer_datos_2

def main():
 while True:
    print("menu de opciones")
    print("1. Calcular salario")
    print("2. Calcular x")
    print("3. Calcular n!")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        horas, pago = leer_datos()
        salario = calcular_salario(horas, pago)
        mostrar_salario(salario)
    elif opcion == "2":
        a, b, c = leer_datos_1()
        x = calcular_x(a, b, c)
        mostrar_x(x)
    elif opcion == "3":
        n = leer_datos_2()
        resultado = calcular_n(n)
        mostrar_resultado(resultado)
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()

