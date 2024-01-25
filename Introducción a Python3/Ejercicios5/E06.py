"""
Crear un personaje que puede luchar contra enemigos. 
En este juego, el jugador tiene un personaje con estadísticas y puede elegir luchar contra enemigos aleatorios. 
El objetivo es derrotar a los enemigos y ganar experiencia.
Este juego permite a un jugador controlar a un personaje que lucha contra enemigos aleatorios. 
El jugador puede atacar o huir durante los encuentros. 
El juego sigue hasta que el personaje o todos los enemigos sean derrotados.
Si el personaje gana suficiente experiencia, se considera que ha ganado el juego. 
Puedes personalizar los nombres y las estadísticas de los personajes y enemigos para hacer el juego más interesante. 
"""
import random

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.ataque = 10
        self.defensa = 5
        self.experiencia = 0


    def atacar(self, enemigo):
        damage = self.ataque - enemigo.defensa
        
        if damage > 0:
            enemigo.vida -= damage
            print(f"{self.nombre} ataca a {enemigo.nombre} y le causa {damage} puntos de daño.")
        else:
            print(f"{self.nombre} ataca a {enemigo.nombre}, pero no causa daño.")


    def ganar_experiencia(self, cantidad):
        cantidad = random.randint(10, 20) 
        self.experiencia += cantidad
        print(f"{self.nombre} ha ganado {cantidad} puntos de experiencia.")

    def esta_vivo(self):
        if self.vida <= 0:  
            print("Has sido derrotado")
            return False
        else:
            return True
    
    def mostrar_estado(self):
        print(f"{self.nombre}: Vida = {self.vida}, Ataque = {self.ataque}, Defensa = {self.defensa}, Experiencia = {self.experiencia}")


class Enemigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 10
        self.ataque = random.randint(5, 15)
        self.defensa = 5
    
    def atacar(self, personaje):
        damage = self.ataque - personaje.defensa

        if damage > 0:
            personaje.vida -= damage
            print(f"{self.nombre} ataca a {personaje.nombre} y le causa {damage} puntos de daño.")
        else:
            print(f"{self.nombre} ataca a {personaje.nombre}, pero no causa daño.")

    def esta_vivo(self):
        if self.vida <= 0:    
            print("Derrotaste al enemigo")
            return False
        else:
            return True   
        
    def mostrar_estado(self):
        print(f"{self.nombre}: Vida = {self.vida}, Ataque = {self.ataque}, Defensa = {self.defensa}")

def main():
    nombre_personaje = input("Ingresa el nombre de tu personaje: ")
    personaje = Personaje(nombre_personaje)
    
    
    while personaje.esta_vivo():
        enemigos = [Enemigo("Orco"), Enemigo("Goblin"), Enemigo("Lobo")]
        enemigo = random.choice(enemigos)
        print(f"\nTe encuentras con un {enemigo.nombre} enemigo.")
    
        while enemigo.esta_vivo() and personaje.esta_vivo():
            print("\nEstado actual:")
            personaje.mostrar_estado()
            enemigo.mostrar_estado()

            accion = input("¿Qué deseas hacer? (atacar/huir): ").lower()
            if accion == "atacar":
                personaje.atacar(enemigo)
        
                if enemigo.esta_vivo():
                    enemigo.atacar(personaje)

            elif accion == "huir":
                print("Escapas del combate.")
                break
        
            else:
                print("Acción no válida. Ingresa 'atacar' o 'huir'.")
    
        if enemigo.vida <= 0:
            experiencia_ganada = random.randint(10, 20)
            personaje.ganar_experiencia(experiencia_ganada)
            print(f"Has derrotado al {enemigo.nombre} enemigo y ganado {experiencia_ganada} puntos de experiencia.")
        
        if personaje.vida <= 0:
            print(f"Has sido derrotado por el {enemigo.nombre} enemigo.")
            print("\nEl juego ha terminado.")
        
        if personaje.experiencia >= 50:
            print(f"{personaje.nombre} ha ganado el juego y se ha convertido en un heroe.")
            break

if __name__ == "__main__":
    main()
