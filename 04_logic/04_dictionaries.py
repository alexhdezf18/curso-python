# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.


# Ejemplo tipico de diccionario
persona = {
    'nombre': 'midudev',
    'edad': 25,
    'es_estudiante': True,
    'calificaciones': [7, 8, 9],
    'socials':{
        'twitter': 'midudev',
        'instagram': '@midudev',
        'facebook': 'midudev'
    }
}

# para acceder a los valores
print(persona['nombre'])
print(persona['calificaciones'][2])

# cambiar valores al acceder
persona['nombre'] = 'madeval'
persona['calificaciones'][2] = 10

print(persona)

# eliminar completamente una propiedad
del persona['edad']
print(persona)

# devuelve el valor y lo elimina
es_estudiante = persona.pop('es_estudiante')
print(f'es_estudiante: {es_estudiante}')
print(persona)

# sobreescribir un diccionario con otro diccionario
a = { 'name': 'midudev', 'age': 25}
b = { 'name': 'madeval', 'es_estudiante': True}

a.update(b)
print(a)

# comprobar si existe una propiedad
print('name' in persona) # False
print('nombre' in persona) # True


# Obtener todas las claves
print("\nkeys:")
print(persona.keys())

# Obtener todos los valores
print("\nvalues:")
print(persona.values())

# Obtener tanto clave como valor
print("\nitems:")
print(persona.items())

for key, value in persona:
    print(f'{key}: {value}')