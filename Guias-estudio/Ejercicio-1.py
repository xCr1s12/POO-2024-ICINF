
class Estudiante():
    def __init__(self,nombre,*notas):
        self.__nombre = nombre
        self.__notas = list(notas)
        self.__promedio = float(sum(self.__notas)/len(self.__notas))
        self.status = self.new_status()
    
    def status_estudiante(self):
        print("el estudiante aprobo" if self.status else "el estudiante reprobo")
    
    def actualizar(self,nota_cambio, nueva_nota):
        self.__notas[nota_cambio] = nueva_nota   
        self.__promedio = float(sum(self.__notas)/len(self.__notas))
    
    def new_status(self):
        return self.__promedio >= 4.0
    
    def __str__(self):
        return f"nombre: {self.__nombre}, promedio: {self.__promedio}"

mat = Estudiante("Mat", 1.5 ,6.0)
teo = Estudiante("Teo", 2.5, 7.0, 3.5)
juan = Estudiante("JUan", 2.5, 7.0, 3.5)

print(mat)
mat.actualizar(1,6.0)
mat.status_estudiante()

print(teo)
teo.status_estudiante()