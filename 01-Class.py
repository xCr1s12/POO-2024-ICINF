class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
            print(f"{self.nombre} estas comiendo")
    

persona1 = Persona(input("Escribe tu nombre"), 19)
persona2 = Persona("matheo", 20)

print(f"Hola {persona1.nombre} tienes {persona1.edad}")
print(f"Hola {persona2.nombre} tienes {persona2.edad}")
persona1.comer()
persona2.comer()