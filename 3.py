"""# Definir la matriz X (lista de listas)
matriz_X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]"""

cantx = int(input("Ingrese la cantidad de filas de la matriz: "))
canty = int(input("Ingrese la cantidad de columnas de la matriz: "))
matriz_X = []
for i in range(cantx):
    fila = []
    for j in range(canty):
        fila.append(int(input("Ingrese el elemento de la fila {} y columna {}: ".format(i+1, j+1))))
    matriz_X.append(fila)

# Calcular la matriz transpuesta XT usando lambda
transpuesta_XT = lambda matriz: list(map(list, zip(*matriz)))

# Obtener la matriz transpuesta
matriz_transpuesta = transpuesta_XT(matriz_X)

# Imprimir la matriz original y la matriz transpuesta
print("Matriz Original:")
for fila in matriz_X:
    print(fila)

print("\nMatriz Transpuesta:")
for fila_transpuesta in matriz_transpuesta:
    print(fila_transpuesta)
