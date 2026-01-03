import math

print("Hello, World!")
print('Esto tambien funciona con una comilla simple')


# Separador de argumentos por defecto es un espacio
print("Python", "es", "genial")

# Separador de argumentos por guión definido por el argumento sep
print("Python", "es", "brutal", sep = "-")

# End por defecto es un salto de linea, se puede cambiar con el argumento end
print("Esto se imprime", end = " ")
print("es una linea")


# F-string para imprimir el valor de una variable
print(f"El valor de pi es {math.pi}")