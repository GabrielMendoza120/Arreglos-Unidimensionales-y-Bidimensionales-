# Programa 2: Suma de elementos
print("--- Suma de Elementos de una Lista ---")

# Creamos una lista vacía para los 5 números
numeros = []

# Leemos 5 números enteros desde el teclado usando un ciclo for
for i in range(5):
    numero = int(input(f"Ingresa el número entero {i + 1}: "))
    numeros.append(numero)

# Inicializamos el acumulador de la suma en cero
suma_total = 0

# Recorremos la lista sumando cada elemento al acumulador
for numero in numeros:
    suma_total += numero

# Mostramos el resultado en la consola
print("\nResultados:")
print(f"Lista de números ingresados: {numeros}")
print(f"La suma total de los elementos es: {suma_total}")
