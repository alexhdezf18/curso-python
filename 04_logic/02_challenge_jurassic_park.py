"""
En Jurassic Park, se ha observado que los dinosaurio carnivoros, como el temible T-Rex, depositan
un numero par de huevos. Imagina que tienes una lista de numeros enteros en la que cada numero
representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnivoros (T-Rex) aquellos 
numeros que son pares.

Objetivo:
Escribe una funcion en Python que reciba una lista de numeros enteros y devuelva la suma total
de los huevos que pertenecen a los dinosaurios carnivoros (es decir, la suma de todos los numeros
pares en la lista).
"""

def count_carnivore_dinosaur_eggs(egg_list) -> int:
    """
    Esta funcion recibe una lista de numeros enteros que representan la cantidad de huevos que
    han puesto diferentes dinosaurios en el parque jurasico y los de numero par son de carnivoros.
    Devuelve un numero con la suma de todos los huevos de carnivoros
    """

    total_carnivore_eggs = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs

    return total_carnivore_eggs

egg_list = [3, 4, 7, 5, 8]
print(count_carnivore_dinosaur_eggs) # 12