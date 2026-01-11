# Bloques de codigo reutilizabes y parametrizables para hacer tareas especificas

"""Definicion de una funcion

def nombre_de_la_funcion(parametro1, parametro2, ...):
    # docstring
    # cuerpo de la funcion
    return valor_de_retorno # opcional

"""

# Ejemplo de una funcion para imprimir algo en la consola
def saludar():
    print("Hola")

def saludar_a(nombre):
    print(f"Hola {nombre}")

saludar_a("midudev")
saludar_a("Alex")


# Funciones con mas parametros
def sumar(a, b):
    suma = a + b
    return suma

result = sumar(2, 3)
print(result)

# Documentar las funciones con docstring (Explicar que hace la funcion dentro del cuerpo de la funcion)
def restar(a, b):
    """Resta dos numeros y devuleve el resultado"""
    return a - b

# Con el docstring puedes acceder a la documentacion que escribiste dentro de la funcion
print(restar.__doc__)

# En la terminal te describe que hace la funcion
help(restar)

# Parametros por defecto
def multiplicar(a, b = 2):
    return a * b

print(multiplicar(2)) # Output : 4
print(multiplicar(2, 3))  # Output : 6

# Argumentos por clave
def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo{edad} años y me identifico como {sexo}")

# parametros son posicionales
describir_persona("midudev", 25, "gato")

# parametros nombrados
describir_persona(sexo="gato", nombre="midudev", edad=25)


# Argumentos con longitud variable(*args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma +=numero
    return suma

print(sumar_numeros(1, 2, 3, 4, 5))


# Argumentso de clave-valor varibale(*kwargs)
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(nombre="madeval", edad=21, country="uruguay")
print("\n")
mostrar_informacion_de(nombre="pheralb", es_sub=True, is_rich=True)