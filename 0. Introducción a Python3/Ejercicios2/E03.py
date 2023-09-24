"""
Write a program that asks for a temperature value in a scale, for example, 273 degrees in Kelvin scale,
and then converts that temperature to the other known scales, in this case, Fahrenheit and Celsius.
The necessary formulas are:
K = 273.1 + ºC
ºF = 1.4 · ºC + 32
"""

celsiusTemperature = float(input("Enter the temperature in ºC:"))

kelvinTemperature = 273.1 + celsiusTemperature
fahrenheitTemperature = 1.4 * celsiusTemperature + 32

print("Temperature in Celsius:", celsiusTemperature, "ºC")
print("Temperature in Kelvin:", kelvinTemperature, "K")
print("Temperature in Fahrenheit:", fahrenheitTemperature, "ºF")