# Definir la lista de enteros
cantidad = int(input("Ingrese la cantidad de números a ingresar: "))
lista_enteros = []
for i in range(cantidad):
    numero = int(input("Ingrese el número: "))
    lista_enteros.append(numero)

# Definir el exponente n
n = 3

# Calcular la potencia n-ésima de cada elemento usando lambda
potencia_n = lambda x: x**n
resultado = list(map(potencia_n, lista_enteros))

# Imprimir la lista original y la lista resultante
print("Lista Original:", lista_enteros)
print("Potencia {}-ésima de cada elemento:".format(n), resultado)
