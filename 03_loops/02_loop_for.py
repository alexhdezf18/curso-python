# Permiten ejecutar un bloque de codigo repetidamente mientra ITERA un iterable o una lista

print("\n Bucle for:")

# Itera una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

# Iterar sobre cualquier cosa que sea editable
cadena = "midudev"
for caracter in cadena:
    print(caracter)

# enumerate()
frutas = ["manzana", "pera", "mandarina"]
for index, fruta in enumerate(frutas):
    print(f"El indice es {index} y la furta es {fruta}")

# bucles anidados
letras = ["a", "b", "c"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")


#break
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for index, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro esta escondido en el indice {index}")
        break


# continue
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    if animal == "loro":
        continue
    print(animal)

# comprension de listas (list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los numeros pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8] if num % 2 == 0]
print(pares)