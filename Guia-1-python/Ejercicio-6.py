import matplotlib.pyplot as plt 
import numpy as np

class Cuerpo(): 
    def __init__(self,velocidad_c,posicion_inicial):
        self.velocidad = velocidad_c
        self.posicion_inicial = posicion_inicial


    def posicion(self,tiempo): # formula de posicion= Xf = xo + velocidad * tiempo
        return self.posicion_inicial +self.velocidad * tiempo 



# aca es con grafico porrsia con el plot
class SimuladorMovimiento():
    def __init__(self,cuerpo,tiempo, intervalos=100):
        self.cuerpo = cuerpo
        self.tiempo = tiempo
        self.intervalos = intervalos 

    def simular(self):
        tiempo_f = np.linspace(0, self.tiempo,self.intervalos) 
        posiciones = [self.cuerpo.posicion(t) for t in tiempo_f] 

        plt.plot(tiempo_f, posiciones, label=" Velocidad = {self.cuerpo.velocidad} m/s")
        plt.xlabel("tiempo (segundos)")
        plt.ylabel("posicion (metros)")
        plt.title("Simulaci贸n MRU")
        plt.grid(True)
        plt.legend()
        plt.show()

pelota = Cuerpo(0, 12)


simu = SimuladorMovimiento(pelota, 20)


print(pelota)


simu.simular()