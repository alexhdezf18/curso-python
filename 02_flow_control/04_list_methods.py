# Los metodos mas importantes para trabajar con listas

import numbers
import os
os.system("clear")

lista1 = ['a', 'b', 'c', 'd']

lista1.append('e') # Añade un elemento al final de la lista
print(lista1)

lista1.insert(1, '@') # Inserta un elemento en la posicion que le indiquemos como primer argumento
# En este caso el elemento que esta en el indice 1 se recorre al siguiente indice
print(lista1)


lista1.extend(['f', 'g'])  # Añade varios elementos al final de la lista
print(lista1)

# Eliminar elemento de la lista

lista1.remove('@') # Eliminar la primera aparicion de la cadena de texto @
print(lista1)


ultimo = lista1.pop() # Eliminar el ultimo elemento de la lista y te lo devuleve
print(ultimo) # Te devuleve el ultimo elemento de la lista
print(lista1) # Ya no aparece el ultimo elemento en la lista

lista1.pop(1)  # Elimina el segundo elemento de la lista ( es el indice 1)
print(lista1)

del lista1[-1] # Eliminar el elemento con el indice que deseas
print(lista1)

lista1.clear()  # Eliminar todos los elementos de la lista
print(lista1)

lista1 = ['panda', 'koala', 'perro', 'gato', 'hamster']
del lista1[1:3] # Elimina de la lista del rango del 1 al 3
print(lista1)


print('Ordenar Listas')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort() # Ordena la lista y modifica la original
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar un alista de cadenas de texto")
frutas = ['manzana', 'pera', 'limon', 'Manzana', 'Pera', 'Limon']
sorted_frutas = sorted(frutas) # Sorted es sensible a las mayusculas y las coloca al inicio de la lista
print(sorted_frutas)


# Mas metodos utilies
animals = ['perro', 'panda', 'koala', 'perro']
print(len(animals)) # Tamaño de las listas -> 4
print(animals.count('perro')) # Cuantas veces aparece el elemento perro -> 2
print('panda' in animals) # Comprueba si hay un panda en al lista -> True
print('hamster' in animals) # -> False


