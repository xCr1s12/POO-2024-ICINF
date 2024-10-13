"""
1. Implementar un sistema básico para gestionar personajes de un
videojuego utilizando programación orientada a objetos.
Cada personaje tendrá un nombre, nivel de vida y puntos de ataque. La
idea es que los personajes puedan interactuar entre ellos, permitiendo
que un personaje ataque a otro, lo que disminuirá su vida. Además,
deberás verificar si un personaje está vivo o no.
Requerimientos:
1. Clase Personaje:
○ Atributos: el nombre del personaje, el nivel de vida del personaje y los
puntos de ataque del personaje.
○ Métodos: un método que permita que el personaje ataque a otro,
disminuyendo la vida del otro personaje según los puntos de ataque del
atacante. Un segundo método, que verifique si el personaje sigue vivo. Debe
devolver True si el nivel de vida es mayor a 0, y False si no. Por último
implementar un método mágico que permita devolver un string que muestre
el estado del personaje (nombre, vida, y ataque).
Instrucciones:
1. Implementar la clase Personaje con los atributos y métodos descritos
anteriormente.
2. Crear al menos dos personajes. Cada personaje debe tener un nombre, vida inicial y
puntos de ataque.
3. Simula un combate entre los personajes haciendo que uno ataque al otro. Después
de cada ataque, se debe mostrar el estado de ambos personajes.
4. Repetir los ataques hasta que uno de los personajes quede sin vida. Utiliza un
método para verificar si el personaje sigue en pie.
"""


class Personaje():
    def __init__(self,nick,life,AD):
        self.nombre = nick
        self.life  = int(life)
        self.AD = int(AD)

    def atack(self,other):
        other.life -= self.AD
        
    def death(self):
        is_alive = True
        if self.life > 0:
            is_alive = True
        else: 
            self.life = 0
            is_alive = False
        return is_alive
         

    def __str__(self):
        return f'Status de {self.nombre} \nVida: {self.life} \nPuntos de ataque: {self.AD}'
    

Godzilla = Personaje("Godzilla", 1000, 100)
Kong = Personaje("Kong", 1000, 250)

Combate = True

while Combate:


    Kong.atack(Godzilla)
    Godzilla.atack(Kong)

    print(Kong)
    print(Godzilla)
    print("####################################") #Linea divisora
    
    if Kong.death() == False:
        Combate =  False
    if Godzilla.death() == False:
        Combate = False
    else:
        Combate = True


    
