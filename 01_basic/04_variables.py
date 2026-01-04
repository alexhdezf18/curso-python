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

# No recomendada forma de asignar variables
name, age, city = "Alex", 20, "Chihuahua"

# Convecion de variables: snake_case
name_of_person = "Alex"
age_of_person = 20
city_of_person = "Chihuahua"

# Convecion de variables: camelCase
nameOfPerson = "Alex"
ageOfPerson = 20
cityOfPerson = "Chihuahua"

# Convecion de variables: PascalCase
NameOfPerson = "Alex"
AgeOfPerson = 20
CityOfPerson = "Chihuahua"


# UPPERCASE para constantes
NAME_OF_PERSON = "Alex"
AGE_OF_PERSON = 20
CITY_OF_PERSON = "Chihuahua"

# Tipado de variables con tipo de dato explicito
is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)