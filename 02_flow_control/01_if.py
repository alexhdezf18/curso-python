# Importamos el modulo del sistema operativo
import os

# Cada vez que ejecutamos el archivo se limpia la terminal
os.system("clear")

# Permite ejecutar ciertos bloques de codigo si se cumplen ciertas condiciones

print("\n Sentencia simple condicional")
edad = 18
if edad >= 18:
    print("Eres mayor de edad")


print("\n Sentencia condicional con else")
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


print("\n Sentencia condicional con elif")
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("No esta calificado")


print("\n Condiciones multiples")
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("Policia")


es_fin_de_semana = False
if not es_fin_de_semana:
    print("Venga midu, que hay que stremear")


print("\n Anidar condiciones")
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a al discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la disco")


# Ejemplo mas facil
if edad < 18:
    print("No puedes entrar a la disco")
elif tiene_dinero:
    print("Puedes ir a la discoteca")
else:
    print("Quedate en casa")

