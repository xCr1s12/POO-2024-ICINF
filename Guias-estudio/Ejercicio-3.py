class Cliente():
    def __init__(self, __nombre, __n_cuenta, __dinero):
        self.__nombre = __nombre
        self.__n_cuenta = __n_cuenta
        self.__dinero = __dinero
        self.__historial = []
    
    def Consulta_saldo(self):
        return print(f"Dinero actual: {self.__dinero}")

    
    def deposito(self,new_deposito):
        self.__dinero += new_deposito
        self.__historial.append(f"Deposito: {new_deposito}")
        print(f"Dinero actual en la cuenta: {self.__dinero}")

    
    def retiro(self, retiro):
        if retiro > self.__dinero:
            print("El retiro es mayor al dinero en la cuenta")
        else:
            self.__dinero -= retiro
            self.__historial.append(f"retiro: {retiro}")
            print("se retiro el dinero exitosamente")

    def __get_Ncuenta(self):
        return self.__n_cuenta
    
    def __Nombre_c(self):
        return self.__nombre
    
    def __Historial_bancario(self):
        return self.__historial

    def __equals__(self, other):
         return self.__n_cuenta == other.__n_cuenta


    def __str__(self):
         return f"Nombre: {self.__nombre}"


class Banco():
    def __init__(self):
        self.__clientes = {

        }

    def new_client(self,cliente):
        if cliente._Cliente__get_Ncuenta() in self.__clientes:
            print("Numero de cuenta en uso")
        else:
            self.__clientes[cliente._Cliente__n_cuenta] = cliente
    
    def Lista_clientes(self):
        for x in self.__clientes.values():
            print(x)
    
    def Historial_cliente(self, cliente):
        for x in self.__clientes.values():
            if x._Cliente__Nombre_c() == cliente:  
                return x._Cliente__Historial_bancario()  
        return None 

cliente1 = Cliente("Juan", 2180021, 5000)
cliente2 = Cliente("esteban", 2180022, 5000)
banco = Banco()

cliente1.deposito(1000)
cliente1.retiro(6000)

banco.new_client(cliente1)
banco.new_client(cliente2)

banco.Lista_clientes()

print(banco.Historial_cliente("Juan"))

print(cliente1 == cliente2)
