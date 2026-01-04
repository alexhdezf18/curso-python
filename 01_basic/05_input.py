# La funcion input() permite obtener datos del usuario a traves de la consola

print("Hola, como te llamas?")
name = input()
print(f"Hola {name}, bienvenido al programa")

age = int(input("Cuantos años tienes?"))
print(f"En 20 años tendras {age + 20}")

print("Obtener multiples valores a la vez")
country, city =  input("En que pais y ciudad vives?").split()
print(f"Vives en {country}, {city}")