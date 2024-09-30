#Definir Clase 
class Persona():
    def __init__(self, nombre, edad, altura, peso):
        #Aqui se definen los atributos
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso


    #Metodo para el imc
    def calcular_imc(self):
        self.IMC = round(self.peso / (self.altura**2) , 2)            
        print(f" tu imc es: {self.IMC} y tienes un estado de:")
        
        #Comparativa
        if self.IMC >= 0 and self.IMC <= 15.99 :
                print ("Delgadez severa")
        elif self.IMC >= 16.00 and self.IMC <= 16.99 :
                print ("Delgadez moderada")    
        elif self.IMC >= 17.00 and self.IMC <= 18.49:
                print ("Delgadez leve")
        elif self.IMC >= 18.50 and self.IMC <= 24.99 :
                print ("Normal")
        elif self.IMC >= 25.00 and self.IMC <= 29.99:
                print ("Sobrepeso")
        elif self.IMC >= 30.00 and self.IMC <= 34.99:
                print ("obesidad leve")                
        elif self.IMC >= 35.00 and self.IMC <= 39.00:
                print ("obesidad media")
        elif self.IMC >= 40.00:
                print ("obesidad morbida")
        return self.IMC
    def promedio_asignatura(self, nota1,nota2,nota3):
           self.promedio =  float((nota1 + nota2 + nota3)/3)
           print(" aprobaste" if self.promedio >= 4.00 else "reprobaste") 
                     
#se usa la clase 
p1 = Persona("Cristobal", 19 , 1.57 , 78)
print(f"Hola {p1.nombre}, tienes {p1.edad}")
p1.calcular_imc()
p1.promedio_asignatura(2.0,2.0,2.0)
