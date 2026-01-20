# Los cuantificadores se utilizan para especificar cuantas ocurrencias de un caracter
# o grupo de caracteres se deben encontrar en una cadena

import re

# *: Puede aparecer 0 o mas veces

text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

# EJERCICIO 1:
# Cuantas palabras tienen de 0 a mas a despues de una b

# +: Una a mas veces
text = "dddd aaa ccc bb"
pattern = "a+"
matches =  re.findall(pattern, text)
print(matches)

# ?: Cero o una vez
text = "aaaba"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

# EJECICIO : Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
pattern = fr"(\+|00)+?34 \d{9}"

# {n}:  Exactamente n veces
text = "aaaaaa"
pattern = f"a{3}"
matches = re.findall(pattern, text)
print(matches)


# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# EJERCICIO:
# Encuentra las palabras de mas de 4 letras
words = "ala casa arbol leon cinco murcielago"
pattern = fr"\b\w{4,6}\b"
matches = re.findall(pattern, text)
print(matches)

# EJERCICIO
# Encuentra las palabras de mas de 6 letras
words = "ala fantastico casa arbol leon cinco murcielago"
pattern = fr"\b\w{6,}\b"
matches = re.findall(pattern, text)
print(matches)