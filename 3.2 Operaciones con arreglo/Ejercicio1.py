
# Definimos la matriz bidimensional (3x3)
matriz = [
    [5, 12, 7],
    [9, 15, 3],
    [14, 2, 8]
]

# Definimos la función para buscar un valor específico en la matriz
def buscar_valor_en_matriz(matriz, valor_a_buscar):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_a_buscar:
                return i, j  # Retorna la posición si se encuentra el valor
    return None  # Retorna None si no se encuentra el valor

# Definimos el valor que queremos buscar
valor = 15

# Llamamos a la función y capturamos el resultado
resultado = buscar_valor_en_matriz(matriz, valor)

# Mostramos el resultado
if resultado:
    print(f"Valor {valor} encontrado en la posición {resultado}.")
else:
    print(f"Valor {valor} no se encontró en la matriz.")


