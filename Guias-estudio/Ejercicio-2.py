import os


class Contacto():
    def __init__(self,nombre, numero, email ):
        self.__nombre = nombre
        self.__numero = numero
        self.__email = email
    
    def __str__(self):
        return f"Nombre: {self.__nombre}\nTelefono: {self.__numero}\nEmail: {self.__email}"
    
    def nombre(self) -> str:
        return self.__nombre
    
    def cambio(self):
        cambio = input("Que desea cambiar: ")
        aux = True
        while aux:
            if cambio.lower() == "email":
                self.__email = input("Ingrese el nuevo email: ")
                aux = False  
            elif cambio.lower() == "telefono":
                self.__numero = int(input("Ingrese el nuevo numero: "))
                aux = False
            elif cambio.lower() == "nombre":
                self.__nombre = input("Ingresa el nuevo nombre de contacto: ")
                aux = False
            else:
                print("Elija una opcion")


class Agenda():
    def __init__(self):
        self.contactos = []
    
    def agregar_contacto(self,new_contacto):
        self.contactos.append(new_contacto) 

    def mostrar_contactos(self) -> none:
        for i in self.contactos:
            print(i.nombre())

    def buscar_contacto(self,busqueda):
        try:
            for x in self.contactos:
                if x.nombre() == busqueda :
                     print(x)
        except:
            print("Contacto no encontrado")
    def actualizar(self,busqueda):
        try:
            for x in self.contactos:
                if x.nombre() == busqueda :
                     x.cambio()
        except:
            print("Contacto no encontrado")
                
    def __del__(self):
        print("cerrando agenda")





agenda = Agenda()
new_aux  = True
opciones = {
    1: "Nuevo Contacto",
    2: "Mostrar Contactos",
    3: "Buscar Contato",
    4: "Actualizar contacto", 
    0: "Cerrar Agenda"
}
print("----------------------------------------")
print("---------------AGENDA-------------------")
print("----------------------------------------")
print("--------------Opciones------------------")
while new_aux:

    try:
            
        for x, i in opciones.items():
            print(x," --> ",i)
        opcion = int(input("Selecione una opcion numerica: "))
        if opcion == 0 :
            new_aux = False
        elif opcion == 1:
            contacto= Contacto(input("Ingresa el nombre del contacto: "), int(input("Ingresa el numero del contacto: ")), input("Ingresa el correo del contacto: "))
            agenda.agregar_contacto(contacto)
            
        elif opcion == 2:
            while True:
                agenda.mostrar_contactos()
                aux = input("presione 1 para salir") 
                if aux == "1":
                    os.system("cls")
                    break
        elif opcion == 3:
            while True:
                agenda.buscar_contacto(input("Ingrese el nombre del contacto: "))
                aux = input("presione 1 para salir") 
                if aux == "1":
                    os.system("cls")
                    break
        elif opcion == 4:
            while True:
                agenda.actualizar(input("Ingrese el nombre del contacto: "))
                aux = input("presione 1 para salir") 
                if aux == "1":
                    os.system("cls")
                    break
                
        else:
            print("seleccion invalida")
    except:    
        print("error")
        aux = input(" desea salir?")
        if aux.lower() == "si":
            break
        elif aux.lower() == "no":
            pass
        else:
            print("opcion invalida")
del agenda