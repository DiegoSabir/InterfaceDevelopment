"""
Crear una clas CuentaBancaria que tenga atributos como titular, saldo y dos método para depositar y retirar dinero. 
Si no tiene saldo debe mostrar el mensaje “saldo insuficiente”. 
Establece un menú
"""
class CuentaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
            self.saldo += cantidad
            print("Depósito de €", cantidad, " realizado con éxito.")

    def retirar(self, cantidad):
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print("Retiro de $", cantidad, " realizado con éxito.")
            else:
                print("Saldo insuficiente para realizar el retiro.")

def main():
    titular = input("Introduzca el nombre del titular de la cuenta:")
    cuenta = CuentaBancaria(titular)

    while True:
        print("\nMenú Cuenta Bancaria:")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Salir")

        opcion = int(input("Introduzca una de las opciones disponibles:"))

        if opcion == 1:
            cantidad = float(input("Introduce la cantidad a depositar:"))
            cuenta.depositar(cantidad)
        elif opcion == 2:
            cantidad = float(input("Introduce la cantidad a retirar:"))
            cuenta.depositar(cantidad)
        elif opcion == 3:
            print("Saliendo del programa")
            break
        else:
            print("ERROR. Opcion no valida")

if __name__ == "__main__":
    main()
