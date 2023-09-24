"""
Codifica un programa “Loterías” que conteña un menú que acceda as seguintes funcións:
1. Un xerador de apostas da primitiva (6 números entre 1 e 49 máis o complementario entre 1 e o 9).
2. Xerador de Euromillóns (5 números entre 1 e 50 máis dous números “estrela” entre 1 e 9).
3. Un xerador de apostas da quiniela de fútbol, 15 resultados entre 1,X,2.
4. Un xerador de Lotería nacional. Un número entre o 00000 e o 99999.
Valorarase que o menú sexa outra función
"""

import random

def primitiva():
    numeros_primitiva = random.sample(range(1, 50), 6)
    complementario = random.randint(1, 9)
    print("Apuesta de La Primitiva:")
    print("Números:", sorted(numeros_primitiva))
    print("Complementario:", complementario)

def euromillones():
    numeros_euromillones = random.sample(range(1, 51), 5)
    estrellas = random.sample(range(1, 10), 2)
    print("Apuesta de Euromillones:")
    print("Números:", sorted(numeros_euromillones))
    print("Estrellas:", sorted(estrellas))

def quiniela():
    quiniela = [random.choice(['1', 'X', '2']) for _ in range(15)]
    print("Apuesta de la Quiniela de fútbol:")
    print("Resultados:", ' - '.join(quiniela))

def loteriaNacional():
    numero_loteria = random.randint(0, 99999)
    print("Número de Lotería Nacional:", str(numero_loteria).zfill(5))

def menu():
    while True:
        print("\nMenú Loterías:")
        print("1. La Primitiva")
        print("2. Euromillones")
        print("3. La Quiniela de fútbol")
        print("4. Lotería Nacional")
        print("5. Salir")

        opcion = input("Selecciona una de las opciones anteriores: ")

        if opcion == '1':
            primitiva()
        elif opcion == '2':
            euromillones()
        elif opcion == '3':
            quiniela()
        elif opcion == '4':
            loteriaNacional()
        elif opcion == '5':
            break
        else:
            print("ERROR. Elija una de las opciones disponibles")

menu()