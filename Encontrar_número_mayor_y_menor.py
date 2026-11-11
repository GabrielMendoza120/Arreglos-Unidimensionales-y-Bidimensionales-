# Programa 3: Encontrar número mayor y menor
print("--- Buscador de Número Mayor y Menor ---")

# Creamos una lista vacía para los 8 números
numeros = []

# Leemos 8 números enteros desde el teclado usando un ciclo for
for i in range(8):
    numero = int(input(f"Ingresa el número entero {i + 1}: "))
    numeros.append(numero)

# Inicializamos el mayor y el menor con el primer elemento de la lista
mayor = numeros[0]
menor = numeros[0]

# Buscamos de manera lógica recorriendo el arreglo
for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

# Mostramos los resultados en la consola
print("\nResultados:")
print(f"Lista de números ingresados: {numeros}")
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
