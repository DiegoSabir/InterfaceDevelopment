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
        else:
            return True
    
    def mostrar_estado(self):
        print(f"{self.nombre}: Vida = {self.vida}, Ataque = {self.ataque}, Defensa = {self.defensa}, Experiencia = {self.experiencia}")


class Enemigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = random.randint(50, 100)
        self.ataque = random.randint(5, 15)
        self.defensa = random.randint(3, 10)
    
    def atacar(self, personaje):
        damage = self.ataque - enemigo.defensa
        if damage > 0:
            personaje.vida -= damage
            print(f"{self.nombre} ataca a {personaje.nombre} y le causa {damage} puntos de daño.")
        else:
            print(f"{self.nombre} ataca a {personaje.nombre}, pero no causa daño.")

    def esta_vivo(self):
        if self.vida <= 0:    
            print("Derrotaste al enemigo")
        else:
            return True   
        
    def mostrar_estado(self):
        print(f"{self.nombre}: Vida = {self.vida}, Ataque = {self.ataque}, Defensa = {self.defensa}")

def main():
    nombre_personaje = input("Ingresa el nombre de tu personaje: ")
    personaje = Personaje(nombre_personaje)

    enemigos = [Enemigo("Orco"), Enemigo("Goblin"), Enemigo("Lobo")]
    
    while personaje.esta_vivo():
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
        
        else:
            print("Has sido derrotado por el {enemigo.nombre} enemigo.")
            print("\nEl juego ha terminado.")
        
        if personaje.experiencia >= 50:
            print(f"{personaje.nombre} ha ganado el juego y se ha convertido en un heroe.")
            break

if __name__ == "__main__":
    main()