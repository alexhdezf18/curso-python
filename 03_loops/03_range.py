# Permite crear una secuencia de numeros. Puede ser utili para for, pero no solo para eso

print("\nrange():")

# Por defecto el range empieza desde el 0
nums = range(5)

# Generando una secuencia de numeros del 0 al 9
for num in range(10):
    print(num)


# range(inicio, fin)
for num in range(5, 10):
    print(num)


# range(inicio, fin, paso)
for num in range(0, 10, 2): # Existe un tercer parametro que define cual va a ser el paso, en este caso de 2 en 2
    print(num)

# Empezando del -5 hasta el 0
for num in range(-5, 0):
    print(num)

# Decrementando el contador
for num in range(10, 0, -1):
    print(range)

# Crear una lista para un rango
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# Seria para hacerlo 5 veces
contador = 0
while contador <= 5:
    print("Hacer algo cinco veces")
    contador += 1

# Lo mismo pero con range
for _ in range(5):
    print("Hacer algo cinco veces")