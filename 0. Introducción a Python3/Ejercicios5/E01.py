"""
Crear dos clases, Libro y Autor, que estén relacionadas. 
La clase Libro debe tener un atributo autor, que sea una instancia de la clase Autor, titulo y precio.
El autor tendra la clase nombre y nacionalidad.
Imprimir los atributos del titulo
"""

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    
class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

def main():
    autor = Autor("Cervantes", "española")
    libro = Libro("El Quijote", autor.nombre, "30.99")

    print("El ", libro.titulo, " lo escribio ", autor.nombre, " y cuesta ", libro.precio)

if __name__ == "__main__":
    main()