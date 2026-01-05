import os
os.system("clear")

# Valores logicos: True (Verdadero) y False (Falso)
# Fundamentales para el control de flujo y la logica en la programacion

# Los booleanos representan valores de verdad: True o False
print("\n Valores booleanos basicos:")
print(True)
print(False)

# Operadores de comparacion devuelven un valor booleano
print("\n Operadores de comparacion:")
print("5 > 3:", 5 > 3)  # True  
print("5 < 3:", 5 < 3)  # False
print("5 == 3:", 5 == 3)# True  
print("5 != 3:", 5 != 3)# True
print("5 >= 3:", 5 >= 3)# True
print("5 <= 3:", 5 <= 3)# False

print("\n Comparacion de cadenas:")
print("manzana < pera", "manzana" < "pera") # True

# Operadores logicos: and, or, not
print("\n Operadores logicos")
print("True and True:", True and True)     # True
print("True and False:", True and False)   # False
print("False and False:", False and False) # False

print("True or True:", True or True)       # True
print("True or False:", True or False)     # True
print("False or False:", False or False)   # False

print("not True:", not True)               # False
print("not False:", not False)             # True

# Ejemplo practico
edad = 20
tiene_entrada = True

puede_entrar = edad >= 18 and tiene_entrada
print("¿Puede entrar a la fiesta?", puede_entrar)
