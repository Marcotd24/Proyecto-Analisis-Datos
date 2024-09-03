# Definición de la matriz 3D (3 ciudades, 7 días, 2 semanas)
# Asegúrate de que las temperaturas son números y no listas
temperaturas = [
    [  # Ciudad 1
        [[30, 32, 31, 29, 28, 30, 31], [31, 33, 32, 30, 29, 31, 32]],  # Semana 1 y 2
    ],
    [  # Ciudad 2
        [[22, 24, 23, 21, 20, 22, 23], [23, 25, 24, 22, 21, 23, 24]],
    ],
    [  # Ciudad 3
        [[15, 17, 16, 14, 13, 15, 16], [16, 18, 17, 15, 14, 16, 17]],
    ]
]

# Número de ciudades, días y semanas
num_ciudades = len(temperaturas)
num_dias = len(temperaturas[0][0])
num_semanas = len(temperaturas[0])

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
for ciudad in range(num_ciudades):
    print(f"Ciudad {ciudad + 1}:")

    for semana in range(num_semanas):
        suma_temperaturas = 0
        for dia in range(num_dias):
            suma_temperaturas += temperaturas[ciudad][0][semana][dia]  # Asegúrate de que el índice está correcto

        promedio_temperaturas = suma_temperaturas / num_dias
        print(f"  Promedio de temperaturas en la semana {semana + 1}: {promedio_temperaturas:.2f}°C")
    print()

