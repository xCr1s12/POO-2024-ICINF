import pygame
import random
import  math

pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laboratorio N°2 - Ejercicio 2")


# Colores
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# FPS (Frames por segundo)
FPS = 60
reloj = pygame.time.Clock()

class Puntos:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.radio = 8  # Tamaño del punto

    def mover(self):
        self.y += self.velocidad
        if self.y > ALTO:  # Se reinicia ka posición cuando el punto rojo sale de la pantalla
            self.reiniciar()

    def reiniciar(self):
        self.x = random.randint(0, ANCHO - self.radio)
        self.y = random.randint(-100, -40)

    def dibujar(self):
        pygame.draw.circle(pantalla, ROJO, (self.x, self.y), self.radio)

# Clase Triángulo

""" IMPLEMENTAR CÓDIGO """

class Triangulo():
    def __init__(self):
        self.x = 400
        self.y = 500
        self.velocity = 5
    def draw(self):
        Triangulo = [(self.x, self.y),( self.x-50,self.y+60),(self.x+45 , self.y+60)]
        pygame.draw.polygon(pantalla, (0,0,255), Triangulo, )
    
    def move(self, keys):
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity

        if keys[pygame.K_LEFT]:
            self.x -= self.velocity

    def collision(self, other):
        distancia = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return distancia <= other.radio



# Función Principal

def main():
    # Creación de la lista de puntos rojos
    puntos_rojos = [Puntos(random.randint(0, ANCHO - 10), random.randint(-100, -40), random.randint(2, 6)) for _ in range(5)]

    corriendo = True
    triangulo = Triangulo() 
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        keys = pygame.key.get_pressed()
        # Limpiar pantalla
        pantalla.fill(NEGRO)
        # Mover y dibujar los puntos rojos
        for punto in puntos_rojos:
            punto.mover()
            punto.dibujar()

            if triangulo.collision(punto):
               corriendo = False
        #Metodos del triangulo
        triangulo.draw()
        triangulo.move(keys)
        

        
        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()
# Iniciar el juego
if __name__ == "__main__":
    main()
