import math
import numpy as np
import matplotlib.pyplot as plt

class Funciontrigonometrica():
    def __init__(self,funcion,amplitud=2,periodo=2 * np.pi):
        self.funcion = funcion
        self.amplitud = amplitud
        self.periodo = periodo

    def evaluar(self,x): # la formula para evaluar es : "amplitud * sen/cos/tan de el valor x en radianes"
        if self.funcion == "seno":
            return self.amplitud * math.sin(x)
        
        elif self.funcion == "coseno":
            return self.amplitud * math.cos(x)
        
        elif self.funcion == "tangente":
            return self.amplitud * math.tan(x)
        
    def grafico(self, inicio=-2 *np.pi, fin=2 * np.pi, puntos=1000 ): # Funcion para crear el grafico
        x = np.linspace(inicio, fin, puntos)

        if self.funcion == "seno":
            y = self.amplitud * np.sin(x * (2*np.pi / self.periodo))
        
        elif self.funcion == "coseno":
            y = self.amplitud * np.cos(x * (2*np.pi / self.periodo))

        elif self.funcion == "tangente":
            y = self.amplitud * np.tan(x * (2*np.pi / self.periodo))

        plt.plot(x,y)
        plt.title(f"Funcion de {self.funcion.capitalize()} (Amplitud: {self.amplitud}, y de Periodo: {self.periodo} )")
        plt.xlabel("Radianes")
        plt.ylabel(self.funcion.capitalize())
        plt.grid(True)
        plt.show()

        def valor_critico(self):
            if self.funcion == "seno" or self.funcion == "coseno":
                return {"maximo": self.amplitud, "minimo": -self.amplitud}
            
            elif self.funcion == "tangente":
                return "La funcion no tiene máximos y tampoco tíene mínimos mínimos."
            
        def __str__(self):
            return f"Funcion {self.funcion.capitalize()} con amplitud {self.amplitud} y periodo {self.periodo}"


fun_seno = Funciontrigonometrica("seno", amplitud=2, periodo=2 * np.pi)

fun_seno.grafico()