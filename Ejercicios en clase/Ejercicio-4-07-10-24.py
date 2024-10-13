class Vehiculo():
    def __init__(self, marca,modelo,año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año 
        self.__disponibilidad = True
        

    def vendido(self,vendido):
        if vendido:
            self.__disponibilidad = True
        else: 
            self.__disponibilidad = False

    def __str__(self):
        return f"marca : {self.__marca} \nmodelo = {self.__modelo} \naño = {self.__año} \ndisponible = {self.__disponibilidad}"


class Concesionaria():
    vehiculos = []
    