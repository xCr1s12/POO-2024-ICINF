class Coche:
    def __init__(self, marca, gasolina):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recorridos = 0

    def conducir(self, kilometros):
        
        gasolina_necesaria = kilometros / 10
        
        # revisarsuficiente gasolina
        if gasolina_necesaria <= self.gasolina:
            self._actualizar_estado(kilometros, gasolina_necesaria)
            print(f"Has conducido {kilometros} kilómetros. Te quedan {self.gasolina} litros de gasolina.")
        else:
            kilometros_posibles = self.gasolina * 10
            self._actualizar_estado(kilometros_posibles, self.gasolina)
            print(f"Te has quedado sin gasolina después de recorrer {kilometros_posibles} kilómetros.")

    def cargar_gasolina(self, litros):
        self.gasolina += litros
        print(f"Has agregado {litros} litros de gasolina. Ahora tienes {self.gasolina} litros de gasolina.")

    def _actualizar_estado(self, kilometros, gasolina_usada):
        self.kilometros_recorridos += kilometros
        self.gasolina -= gasolina_usada

#uso de la clase coche
mi_coche = Coche("chevrolet", 10)  # Creamos un coche (objeto) con 10 litros de gasolina

# Conducimos 50 kilómetros
mensaje = mi_coche.conducir(50)


mensaje = mi_coche.conducir(60)


mensaje = mi_coche.cargar_gasolina(5)



mensaje = mi_coche.conducir(30)
 