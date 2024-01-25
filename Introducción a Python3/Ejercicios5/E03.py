"""
Diseña una agenda de contacto con una clase Contacto que represente a una persona con atributos 
como nombre, dirección de correo electrónico y número de teléfono. 
Luego, crea una clase Agenda que almacene una lista de contactos y ofrezca métodos para agregar, eliminar y buscar contactos. 
Utiliza encapsulamiento para proteger los datos de contacto. 
Establece un menú.
"""

class Contacto:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def getNombre(self):
        return self.nombre

    def getEmail(self):
        return self.email

    def getTelefono(self):
        return self.telefono

    def __str__(self):
        return f"Nombre: {self.nombre}\nEmail: {self.email}\nTeléfono: {self.telefono}\n"


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar(self, contacto):
        self.contactos.append(contacto)

    def eliminar(self, nombre):
        for contacto in self.contactos:
            if contacto.getNombre() == nombre:
                self.contactos.remove(contacto)
                return True
        return False

    def buscar(self, nombre):
        for contacto in self.contactos:
            if contacto.getNombre() == nombre:
                return contacto
        return None

def main():
    agenda = Agenda()

    while True:
        print("\nMenú Agenda:")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Salir")

        opcion = int(input("Introduzca una de las opciones:"))

        if opcion == 1:
            nombre = input("Introduzca el nombre: ")
            email = input("Introduzca el correo electrónico: ")
            telefono = int(input("Introduce el número de telefoon: "))
            nuevoContacto = Contacto(nombre, email, telefono)
            agenda.agregar(nuevoContacto)
            print("Nuevo contacto agregado")

        elif opcion == 2:
            nombre = input("Introduzca el nombre del contacto: ")

            if agenda.eliminar(nombre):
                print("Contacto eliminado")
            else:
                print("Contacto no encontrado.")

        elif opcion == 3:
            nombre = input("Introducca el nombre del contacto: ")
            contacto = agenda.buscar(nombre)

            if contacto:
                print("Contacto encontrado:")
                print(contacto)
            else:
                print("Contacto no encontrado.")

        elif opcion == 4:
            print("Saliendo del programa")
            break
        
        else:
            print("ERROR. Opcion no valida")

if __name__ == "__main__":
    main()
