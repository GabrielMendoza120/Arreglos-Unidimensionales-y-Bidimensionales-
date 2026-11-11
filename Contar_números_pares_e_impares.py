# Programa 1: Contar números pares e impares
print("--- Contador de Pares e Impares ---")

# Creamos una lista vacía para almacenar los números
numeros = []

# Leemos 10 números enteros desde el teclado usando un ciclo for
for i in range(10):
    numero = int(input(f"Ingresa el número entero {i + 1}: "))
    numeros.append(numero)

# Inicializamos los contadores en cero
pares = 0
impares = 0

# Recorremos la lista para evaluar cada número
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostramos los resultados en la consola
print("\nResultados:")
print(f"Lista de números ingresados: {numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
