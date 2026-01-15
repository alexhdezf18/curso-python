# Metacaracteres

# Los metacaracteres son simbolos especiales con significados especificos en las 
# expresones regulares

import re

# 1. El punto (.)
# Coincidir con cualquier caracter excepeto una nueva linea
text = "Hola mundo, H0la de nuevo, h0la otra vez"
pattern = "H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if(found):
    print(found)
else:
    print("No se ha encontrado el patron")


# El punto solo sustituye un solo caracter
text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)
print(matches)

# ---------------------------------------------------

text = "Hola mundo, H0la de nuevo, h0la otra vez"
# La r indica que estamos utilizando una expresion regular
pattern = r"H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)
if(found):
    print(found)
else:
    print("No se ha encontrado el patron")

# Como usar la barra invertida para anular el significado especial de un simbolo
text = "Mi casa es blanca. Y el coche es negro"
pattern = r"\."

matches = re.findall(pattern, text)
print(matches)


# \d: esto coincide con cualquier digito del (0-9)
text = "El numero de telefono es 123456789"
found = re.findall(fr'\d{9}', text)

print(found)

# Ejercicio: Detectar si hay un numero de España en el texto gracias el prefijo +34

text = "Mi numero de telefono es +34 123456789 apuntalo vale?"
pattern = fr"\+34 \d{9}"
found = re.search(pattern, text)
if found: print(f"Encontre el numero de telefono {found.group()}")

# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: Coincide con cualquier espacio en blanco (espacio, tabulacion, salto de linea)
text = "Hola mundo\n Como estas\n"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^: Coincide con el principio de una cadena
text = "423_name"
pattern = "^\w" # validad un nombre de usuario

valid = re.search(pattern, text)

if valid: print("El nombre de usuario es valido")
else: print("El nombre de usuario no es valido")

phone = "+34 123456789"
pattern = fr"^\+\d{1,3} "

valid = re.search(pattern, phone)

# $: Coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$"

valid = re.search(pattern, text)

if valid: print("La cadena es valida")
else: print("La cadena no es valida")

# EJERCICIO
# Calida que un correo sea de gmail

text = "miduga@gmail.com"
pattern = r"^\w+gmail.com$"
valid = re.search(pattern, text)

if valid: print("El correo es gmail valido")
else: print("El correo de gmail es invalido")

# \b: Coincide con el principio o el final de una palabra
text = "casa casada casado casa"
pattern = r"\bcasa\b"

found = re.findall(pattern, text)
print(found)

# |: Coincidir con una opcion u otra
fruits = "platano, manzana, aguacate, palta, pera"
pattern = r"palta|aguacate"

matches = re.findall(pattern, fruits)
print(matches)