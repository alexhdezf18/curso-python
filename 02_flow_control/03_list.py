# Secuencias mutables de elementos
# Pueden contener elementos de diferentes tipos


# Creacion de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "platanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]]
matrix = [[1, 2], [3, 4], [5, 6]]


# Acceso a elementos por indice
print("\nAcceso a elementos por indice")
print(lista2[0]) # manzanas
print(lista2[1]) # peras
print(lista2[-1]) # platanos

# Acceder elementos de una lista dentro de otra lista
print(lista_de_listas[1][0])


# Slicing (rebanado)
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4])  #output: [2, 3, 4]
print(lista1[:3])  #output:  [1, 2, 3]
print(lista1[3:])   #output: [4, 5]
print(lista1[:])    # Hace una copia exacta de la lista

# Se agrega un tercer parametro para el paso
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # para devolver solo indices pares     output: [1, 3, 5, 7]
print(lista1[::-1])  # devuleve una copia de la lista invertida


# Modificar la lista
lista1[0] = 110   # Modifica el primer indice por un 110
print(lista1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

# Concatenacion simple
lista1 = lista1 + [4, 5, 6]
print(lista1)

# Concatenacion reducida (mas eficiente y mas corta)
lista1 += [7, 8, 9]
print(lista1)
           