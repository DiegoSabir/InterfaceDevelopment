"""
Diseña un sistema de clases para simular una tienda. 
Debes tener clases para representar productos, carritos de compra y clientes. 
Los productos deben tener atributos como nombre, precio y cantidad en stock. 
Los clientes deben poder agregar productos a su carrito de compra y realizar compras. 
El carrito de compra debe mantener un registro de los productos y calcular el total de la compra
"""

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class CarritoCompra:
    def __init__(self):
        self.productos = []

    def agregar(self, producto, cantidad):
        if cantidad <= producto.stock:
            self.productos.append((producto, cantidad))
            producto.stock -= cantidad
            print("Añadido al carrito.")
        else:
            print("No hay stock")

    def calcular(self):
        total = 0
        for producto, cantidad in self.productos:
            total += producto.precio * cantidad
        return total

    def registro(self):
        print("\nRegistro del carrito:")
        for producto, cantidad in self.productos:
            print("Producto:", producto.nombre, " - Cantidad:", cantidad)

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = CarritoCompra()

    def comprar(self):
        total = self.carrito.calcular()
        print("\nTotal: $ ", total)
        confirmacion = input("Confirme la compra: (si/no):")
        
        if confirmacion.lower() == 'si':
            print("Compra finalizada")
        
        else:
            print("Compra cancelada. Los productos han sido devueltos al stock.")
            for producto, cantidad in self.carrito.productos:
                producto.stock += cantidad
            self.carrito.productos = []

def main():
    producto1 = Producto("Victoria III", 49.99, 0)
    producto2 = Producto("Crusaders Kings III", 29.99, 10)
    producto3 = Producto("Europa Universalis V", 39.99, 1)

    cliente1 = Cliente("Diego")
    cliente2 = Cliente("Pablo")

    cliente1.carrito.agregar(producto1, 1)
    cliente1.carrito.agregar(producto3, 1)
    cliente2.carrito.agregar(producto2, 1)

    cliente1.carrito.registro()
    cliente1.comprar()

if __name__ == "__main__":
    main()
