# Programa 5: Suma de matrices
print("--- Suma de Matrices 2x2 ---")

# Inicializamos las dos matrices con ceros para poder asignar valores por índice
matriz_a = [[0, 0], [0, 0]]
matriz_b = [[0, 0], [0, 0]]
matriz_resultado = [[0, 0], [0, 0]]

# Lectura de la Matriz A
print("\n--- Ingreso de datos para Matriz A ---")
for fila in range(2):
    for columna in range(2):
        matriz_a[fila][columna] = int(input(f"Matriz A [{fila}][{columna}]: "))

# Lectura de la Matriz B
print("\n--- Ingreso de datos para Matriz B ---")
for fila in range(2):
    for columna in range(2):
        matriz_b[fila][columna] = int(input(f"Matriz B [{fila}][{columna}]: "))

# Cálculo de la suma de ambas matrices
for fila in range(2):
    for columna in range(2):
        matriz_resultado[fila][columna] = matriz_a[fila][columna] + matriz_b[fila][columna]

# Mostrar resultados en la consola
print("\nMatriz A:")
for fila in matriz_a:
    print(fila)

print("\nMatriz B:")
for fila in matriz_b:
    print(fila)

print("\nMatriz Resultante (A + B):")
for fila in matriz_resultado:
    print(fila)
