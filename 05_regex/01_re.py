# Expresiones regulares


"""
Las expresiones regulares son una secuencia de caracteres que forman un patron de busqueda. 
Se utilizan para la busquda de cadenas de texto, validacion de datos, etc.

Porque aprender Regex?

- Busqueda Avanzada: Encontrar patrones especificos en textos grandes de forma rapida y precisa.
(un editor de Markdown solo usando Regex)

- Validacion de datos: Asegurarte que los datos que ingresa un usuario como el email, telefono,
etc. son correctos.

- Extraccion de informacion: Permitir obtener y aprovechar datos especificos de un texto, como 
nombres, fechas, o direcciones.

- Manipulacion del texto: Extraer, reemplazar y modificar partes de la cadena de texto facilmente

"""


# 1. Importar el modulo de expresiones regulares "re"
import re

# 2. Crear un patron, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"

# 3. El texto donde queremos buscar
text = "Hola mundo"

# 4. Usar la funcion de busqueda "re"
result = re.search(pattern, text)

if result:
    print("He encontrado el patron en el texto")
else:
    print("No he encontrado el patron del texto")


# .group() devuleve la cadena que coincide el pattern
print(result.group())

# .start() devolver la posicion inicial de la coincidencia
print(result.start())

# .end() devolver la posicion final de la coincidencia
print(result.end())

# EJERCICIO 01

# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posicion empieza y termina la coincidencia

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la puede cagar con las Regex para in con cuidado"
pattern = "IA"

found_ia = re.search(pattern, text)

if(found_ia):
    print(f'He encontrado el patron en el texto en la posicion {found_ia.start()} y termina en la posicion {found_ia.end()}')
else:
    print("No he encontrado el patron en el texto")


# -------------------------------------------------

# Encontrar todas las coincidencias de un patron 
# .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil. ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)

print(len(matches))


# ---------------------------------------------------

# iter() devulve un iterador que contiene todos los resultados de la busqueda

text = "Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil. ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

# ------------------------------------------------------

# MODIFICADORES

# Los modificadores son opciones que se pueden agregar a un patron para cambiar su
# comportamiento 

# re.IGNORECASE: ignora las mayusuclas y minusculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. Viva la Ia"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

if found: print(found)

# -------------------------------------------------------

# Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patron en un texto

text = "Hola, mundo! Hola de nuevo."
pattern = "Hola"
replacement = "Adios"

new_text = re.sub(pattern, replacement, text)
print(new_text)