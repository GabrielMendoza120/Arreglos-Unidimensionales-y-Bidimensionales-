# Programa 4: Invertir elementos
print("--- Invertir el Orden de una Lista ---")

# Creamos una lista vacía para los 6 números
numeros = []

# Leemos 6 números enteros desde el teclado usando un ciclo for
for i in range(6):
    numero = int(input(f"Ingresa el número entero {i + 1}: "))
    numeros.append(numero)

# Creamos una nueva lista para almacenar el orden invertido
lista_invertida = []

# Recorremos la lista original desde el último elemento (índice 5) hasta el primero (índice 0)
for i in range(5, -1, -1):
    lista_invertida.append(numeros[i])

# Mostramos los resultados en la consola
print("\nResultados:")
print(f"Lista original:  {numeros}")
print(f"Lista invertida: {lista_invertida}")
