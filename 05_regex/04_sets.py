import re
# [: Coincide con cualquier caracter dentro de los corchestes

username = "rub.ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match:
    print("El nombre de ussuarioes valido: ", match.group())
else:
    print("El nombre de usuario no es valido")

# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)


# Una Regex para encontrar las palabras man, fan y ban
# pro ignora el resto

text = "man ran fan ñan ban omniman"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)

# [^] Coincide con cualquier caracter que no este dentro de los corchestes

pattern = r"[^aeiou]"