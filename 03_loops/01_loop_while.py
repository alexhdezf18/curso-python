# PErmiten ejecutar un bloque de codigo repetidamente mientras se cumpla una condicion

from contextlib import ContextDecorator


print("\n Bucle while:")

# Bucle con una simple condicion
contador = 0
while contador < 5:
    print(contador)
    contador += 1 # Esto es super inportante para evitar los bucles infinitos

# el break es una palabra especial para romper el bucle

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break # sale del bucle


# continue, que lo hace es saltar esa iteracion en con
# y continaur con el bucle
print("\n Bucle conb continue")
contador = 0
while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)


# else, esta condicion cuando se ejecuta?
print('\n Bucle while con else:')
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")



# pedirle al ususario un numero que tiene que ser positivo si no, no le dejamos pasar

numero = -1
while numero <= 0:
    numero = int(input("Escribe un numero positivo:"))
    if numero <  0 :
        print("El numero deve ser positivo, Intenta otra vez majo o maja")
print(f'El numero que has introducido es {numero}')



numero = -1
while numero <= 0:
    try:
        numero = int(input("Escribe un numero positivo:"))
        if numero <  0 :
            print("El numero deve ser positivo, Intenta otra vez majo o maja")
    except:
        print(f"Lo que introduces debe ser un numero, que si no peta!")
print(f'El numero que has introducido es {numero}')
