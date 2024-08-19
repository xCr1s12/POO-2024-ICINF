b = input("Escribe tu nombre")
c = input("Escribe tu edad")
class Persona():
    nombre = b
    edad = c 

    def comer(self):
        print(f"{self.nombre} estas comiendo ")

Persona1 = Persona()

print(f"Hola {Persona1.nombre} tienes {Persona.edad}")
Persona1.comer()