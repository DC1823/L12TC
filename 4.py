"""# Función para eliminar elementos de la lista usando lambda
eliminar_elementos = lambda lista, elementos_a_borrar: list(filter(lambda x: x not in elementos_a_borrar, lista))

# Lista original
lista_original = [1, 2, 3, 4, 5, 6]

# Elementos a borrar
elementos_a_borrar = [2, 4, 6]"""

eliminar_elementos = lambda lista, elementos_a_borrar: list(filter(lambda x: x not in elementos_a_borrar, lista))

input1 = int(input("Ingrese la cantidad de elementos de la lista original: "))
lista_original = []
for i in range(input1):
    lista_original.append(int(input("Ingrese el elemento: ")))
input2 = int(input("Ingrese la cantidad de elementos a borrar: "))
elementos_a_borrar = []
for i in range(input2):
    elementos_a_borrar.append(int(input("Ingrese el elemento: ")))



# Aplicar la función y obtener la lista resultante
lista_resultante = eliminar_elementos(lista_original, elementos_a_borrar)

# Imprimir resultados
print("Lista Original:", lista_original)
print("Elementos a Borrar:", elementos_a_borrar)
print("Lista Resultante:", lista_resultante)
