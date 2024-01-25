"""
Escribe un programa que solicite la fecha de 
nacimiento de un usuario y calcule su edad actual.
"""

import datetime

fechaNacimientoString = input("Introduzca su fecha de nacimiento(YYYY-MM-DD):")

fechaNacimiento = datetime.datetime.strptime(fechaNacimientoString, "%Y-%m-%d")

fechaActual = datetime.datetime.now()

edad = fechaActual.year - fechaNacimiento.year

print("Edad:", edad, " años")
