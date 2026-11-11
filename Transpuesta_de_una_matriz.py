# Programa 6: Transpuesta de una matriz
print("--- Transpuesta de una Matriz 3x3 ---")

# Inicializamos la matriz original y la transpuesta con ceros
matriz_original = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz_transpuesta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Lectura de la matriz original
print("\n--- Ingreso de datos para la Matriz 3x3 ---")
for fila in range(3):
    for columna in range(3):
        matriz_original[fila][columna] = int(input(f"Ingresa valor para [{fila}][{columna}]: "))

# Calculamos la transpuesta intercambiando las posiciones (fila por columna)
for fila in range(3):
    for columna in range(3):
        matriz_transpuesta[columna][fila] = matriz_original[fila][columna]

# Mostramos la matriz original en consola
print("\nMatriz Original:")
for fila in matriz_original:
    print(fila)

# Mostramos la matriz transpuesta en consola
print("\nMatriz Transpuesta:")
for fila in matriz_transpuesta:
    print(fila)
