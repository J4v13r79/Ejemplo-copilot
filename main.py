from Soluciones.Salario_semanal import calcular_salario, mostrar_salario, leer_datos

def main():
    horas, pago = leer_datos()
    salario = calcular_salario(horas, pago)
    mostrar_salario(salario)

if __name__ == "__main__":
    main()