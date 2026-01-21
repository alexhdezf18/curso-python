# Trabajando con fechas y horas en Python

from ctypes import FormatError
from datetime import datetime, timedelta


# 1. Obtener la fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual: {now}")

# 2. Crear una fecha y hora especifica
specific_date = datetime(2025, 2, 12)
print(f"Fecha y hora especifica: {specific_date}")

# 3. Formatear fechas
# metodo strftime() para formatear fechas 
# pasarle el objeto datetime y el formato especificado 
# formato:

#Esto hace que las fechas las hace en formato español
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
format_date = now.strftime("%A  %B  %Y %H:%M:%S")
print(f"Fecha formateada: {format_date}")

# 4. Operaciones con fechas(sumar/restar dias, minutos, horas, meses)
yesterday = datetime.now() - timedelta(days= 1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days= 1)
print(f"Mañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours= 1)
print(f"Una hora despues: {one_hour_after}")

# 5. Obtener componenetes individuales de una fecha
year = now.year
print(year)

month = now.month
print(month)

# 6. Calcular la diferencia entre dos feches
date1 = datetime.now()
date2 = datetime(2026, 2, 27, 15, 30, 0)
difference = date2 - date1
print(f"La direncia entre las fechas: {difference}")