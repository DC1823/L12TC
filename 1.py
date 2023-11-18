#Ingresar diccionario
"""ingresecantidadclave = int(input("Ingrese la cantidad de claves que desea ingresar: "))
diccionario = {}
for i in range(ingresecantidadclave):
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor: ")
    diccionario[clave] = valor

"""
lista_diccionarios = [{'make': 'Nokia', 'model': '216', 'color': 'Black'},
                        {'make': 'Apple', 'model': '2', 'color': 'Silver'},
                        {'make': 'Huawei', 'model': '50', 'color': 'Gold'},
                        {'make': 'Samsung', 'model': '7', 'color': 'Blue'}]


# Clave por la cual ordenar los diccionarios
clave_ordenamiento = input("Ingrese la clave por la cual ordenar los diccionarios: ")

# Ordenar la lista de diccionarios usando lambda
lista_ordenada = sorted(lista_diccionarios, key=lambda x: x[clave_ordenamiento])

# Imprimir la lista ordenada
print("Lista Original:")
print(lista_diccionarios)
print("\nLista Ordenada por '{}'".format(clave_ordenamiento))
for diccionario in lista_ordenada:
    print(diccionario)
