# Definimos la matriz bidimensional (3x3)
matriz = [
    [5, 12, 7],
    [9, 15, 3],
    [14, 2, 8]
]

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()  # Para una separación entre la matriz original y la ordenada

# Implementamos Bubble Sort para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila_index):
    fila = matriz[fila_index]
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    matriz[fila_index] = fila

# Mostramos la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

fila_a_ordenar = 1

# Ordenamos la fila especificada
ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz después de ordenar la fila
print(f"Matriz después de ordenar la fila {fila_a_ordenar + 1}:")
imprimir_matriz(matriz)
