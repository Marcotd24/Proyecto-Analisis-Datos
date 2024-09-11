# Función para calcular el promedio de temperatura
def calcular_promedio_temperatura(temperaturas):
    promedios = {}

    # Para cada ciudad en el diccionario de temperaturas
    for ciudad, temp_semanal in temperaturas.items():
        promedio = sum(temp_semanal) / len(temp_semanal)
        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso: Datos de temperaturas (3 ciudades durante 4 semanas)
datos_temperaturas = {
    "Ciudad_A": [20, 22, 19, 21],
    "Ciudad_B": [25, 24, 26, 23],
    "Ciudad_C": [30, 31, 29, 28]
}

# Llamar a la función para calcular los promedios
promedios_ciudades = calcular_promedio_temperatura(datos_temperaturas)

# Imprimir los resultados
for ciudad, promedio in promedios_ciudades.items():
    print(f"El promedio de temperatura en {ciudad} es: {promedio:.2f}°C")
