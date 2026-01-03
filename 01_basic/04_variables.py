# Asignar una variable

my_name = "Alex"
print(my_name)

my_age = 20
print(my_age)

# Reasignar el valor de una variable, se puede reasignar el valor en tiempo de ejecucion
my_age = 21
print(my_age)

# Las variables se pueden reasignar en cualquier tipo de dato, pythoin es un lenguaje de tipado dinamico
my_name = 32


# Tipado fuerte: no realiza conversiones de tipos de datos automáticamente
print(10 + "1") # Esto da un error

# F-string para imprimir el valor de una variable
print(f"Hola mi nombre es {my_name} y mi edad es {my_age}")