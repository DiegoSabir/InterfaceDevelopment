"""
Escribir un programa que lle pida ao usuario seu peso (en kg) e estatura (en metros), 
calcule o índice de masa corporal e o almacene nunha variable <imc> mostrando
por pantalla a frase: Teu índice de masa corporal é <imc>, con dos decimales.

Fórmula: imc = peso/estatura2
"""
weight = float(input("Enter the weight(kg): "))
height = float(input("Enter the height(m): "))

imc = weight / (height ** 2)

print(f"Your body mass index is: {imc:.2f}")