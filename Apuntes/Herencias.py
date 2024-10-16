class Vehiculo():
    def __init__(self,Marca, Modelo, Año_F):
        self.marca = Marca
        self.modelo = Modelo
        self.Año_Fabricacion = Año_F

class Moto(Vehiculo):
    def __init__(self, Marca, Modelo, Año_F,manillar):
        super().__init__(Marca, Modelo, Año_F)
        self.manillar = manillar
    
    
    def __repr__(self):
        return f"marca:  {self.marca} \nModelo: {self.modelo} \naño de fabricacion: {self.Año_Fabricacion} \nManillar: {self.manillar} "

class Auto(Vehiculo):
    def __init__(self, Marca, Modelo, Año_F,n_puertas):
        super().__init__(Marca, Modelo, Año_F)
        self.n_puertas = n_puertas
    
    def __repr__(self):
        return f"marca:  {self.marca} \nModelo: {self.modelo} \naño de fabricacion: {self.Año_Fabricacion} \nNumero de puertas: {self.n_puertas} "
    
moto =  Moto("nAzus" , "G3000", 1990, "oro")
print(repr(moto))

autito = Auto("ford" , "ruso", 1992, 4)
print(repr(autito))