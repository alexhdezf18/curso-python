"""
Esta en equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantasticos, la union y el equilibrio entro los poderes es
fundamental para enfrentar cualquier desafio. En este problema, nos centraremos en
dos de sus miembros:

Reed Richards(Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo: Crea una funcion en Python que reciba una cadena de texto. Esta funcion debe contar
cuantas veces aparece la letra R (para Reed Richards) y cuantes veces aparece la letra J
(para Johnny Storm) en la cadena

- Si la cantidad de Ry la cantidad de J son iguales, se considera que la alianza entre
la mente y el fuego esta en equilibrio y la funcion debe retornar True.
- Si las cantidades no son iguales, la funcion debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende
que el equilibrio se mantiene (0 = 0), por lo que la funcion debe retornar True.
"""

def check_is_balanced(text):
    text = text.upper()

    # contar facilmente el numero de veces que aparece una letra
    count_r = text.count("R") # Reed Richards
    count_j = text.count("J") # Johnny Storm
    
    print(f"count_r: {count_r} count_j: {count_j}")

    return count_r == count_j