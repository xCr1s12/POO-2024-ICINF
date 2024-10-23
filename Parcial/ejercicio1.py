class Gato():
    def __init__(self, nombre: str, raza: str, color: str, edad: int):
        self.nombre = nombre 
        self.__color = color
        self.__raza = raza
        self.__energia = 100
        self.hambre = 100 
        self.__estado = "Feliz"
        self.edad = edad
    def acariciar(self):
        self.__energia += 10
        print("has acariciado al gato y le restauras 10 puntos de energia")
    def jugar(self):
        if self.__energia <= 0:
            print("el gato no tiene energia")
        elif self.__energia < 10 and self.__energia > 0:
            print("energia insuficiente")
        elif self.__energia >= 10:
            self.hambre -= 5 
            self.__energia -= 10
            self.__estado = "jugando"
            print("jugaste con el gato")

    def alimentar(self):
        self.hambre += 10
        self.__energia -= 5
        self.__estado = "comiendo"
        print("alimentaste al gato")


    def __repr__(self) -> str:
        return f"Nombre del gato: {self.nombre},color: {self.__color},Raza : {self.__raza}, energia: {self.__energia},hambre: {self.hambre}, estado: {self.__estado}"
    def __str__(self):
        return f"Nombre del gato: {self.nombre},color: {self.__color},edad : {self.edad}, energia: {self.__energia},hambre: {self.hambre}, estado: {self.__estado}"
    



class Inventario():
    def __init__(self):
        self.__inv  = {
            "comida" : {},
            "juguete" : {}
        }
    
    def agregar_producto(self, tipo, producto, cantidad):
        if tipo.lower() == "comida":
            self.__inv["comida"].update({producto : cantidad})
            print("agregado")
        elif tipo.lower() == "juguete":
            self.__inv["juguete"].update({producto : cantidad})
            print("agregado")
        else:
            print("error")
    def alimentar_gato(self, gato, comida):
        for x, i in self.__inv.items():
            if x == "comida":
                for z, j in zip(i , i.values()):
                    if z == comida and i > 0:
                        gato.alimentar()
                        j -=1
                    else:
                        print("cantidad de alimento insuficiente")
                         
    def jugar_con_gato(self, gato, juguete):
        for x, i in self.__inv.items():
            if x == "juguete":
                for z, j in zip(i , i.values()):
                    if z == juguete and j > 0:
                        gato.jugar()
                        j -= 1
                    else: 
                        print("cantidad insuficiente del juguete")
                         
    def estado(self):
        print(self.__inv)


class Areas():
    def __init__(self):
        self.area1 = []
        self.area2 = []
        self.area3 = []
    
    def agregar_gato_area(self, gato: object, area: int):
        if area == 1:
            if len(self.area1) <= 3:
                self.area1.append(gato)
                print("agregaste un gato")
            else:
                print("el area esta llena")

        elif area == 2:
            if len(self.area2) <= 3:
                self.area2.append(gato)
                print("agregaste un gato")
            else:
                print("el area esta llena")

        elif area == 3:
            if len(self.area3) <= 3:
                self.area3.append(gato)
                print("agregaste un gato")
            else:
                print("el area esta llena")

        else:
            print("area no encontrada")
    def listar(self, area: int):
        if area == 1: 
            print("area 1")
            for x in self.area1:
                print(x)
        elif area == 2:
            print("area 2")
            for x in self.area2:
                print(x)
        elif area == 3:
            print("area 3")
            for x in self.area3:
                print(x)
        else: 
            print("area invalida")
    

inv = Inventario()

areas = Areas()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
pepe1 = Gato("pepeto", color="cafe con manchas", raza="yo ke se", edad= 12)
pepe2 = Gato("pepito", color="cafe con manchas", raza="yo ke se", edad= 12)
pepe3 = Gato("pepote", color="cafe con manchas", raza="yo ke se", edad= 12)
pepe4 = Gato("pepa", color="cafe con manchas", raza="yo ke se", edad= 12)
pepe5 = Gato("pipo", color="cafe con manchas", raza="yo ke se", edad= 12)
pepe6 = Gato("patata", color="cafe con manchas", raza="yo ke se", edad= 12)
pepe7 = Gato("patatita", color="cafe con manchas", raza="yo ke se", edad= 12)
pepe8 = Gato("payaso", color="cafe con manchas", raza="yo ke se", edad= 12)
pepe9 = Gato("juan", color="cafe con manchas", raza="yo ke se", edad= 12)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
pepe3.acariciar()
pepe1.acariciar()
pepe2.acariciar()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#esta es la representacion completa del gato
print(repr(pepe1))
print(repr(pepe2))
print(repr(pepe3))
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
inv.agregar_producto(tipo="comida", producto="atun", cantidad=12)

inv.agregar_producto(tipo="comida", producto="pescado", cantidad=12)

inv.agregar_producto(tipo="comida", producto="ratones", cantidad=12)

inv.agregar_producto(tipo="juguete", producto="bola", cantidad=1)

inv.jugar_con_gato(gato=pepe1, juguete="bola")
inv.jugar_con_gato(gato=pepe1, juguete="bola")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
inv.estado()

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
areas.agregar_gato_area(pepe1, area=1)
areas.agregar_gato_area(pepe2, area=1)
areas.agregar_gato_area(pepe3, area=1)
areas.agregar_gato_area(pepe7, area=2)
areas.agregar_gato_area(pepe8, area=2)
areas.agregar_gato_area(pepe9, area=2)
areas.agregar_gato_area(pepe4, area=3)
areas.agregar_gato_area(pepe5, area=3)
areas.agregar_gato_area(pepe6, area=3)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
areas.listar(area=1)
areas.listar(area=2)
areas.listar(area=3)