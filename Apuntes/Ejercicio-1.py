

class Cliente():
    def __init__(self, __nombre, __n_cuenta, __dinero):
        self.__nombre = __nombre
        self.__n_cuenta = __n_cuenta
        self.__dinero = __dinero
        self.__historial = [""]
    
    def Consulta_saldo(self):
        return print(f"Dinero actual: {self.__dinero}")

    
    def deposito(self,new_deposito):
        self.__dinero += new_deposito
        print(f"__Dinero actual en la cuenta: {self.__dinero}")
    
    def retiro(self, retiro):
        if retiro > self.__dinero:
            print("El retiro es mayor al dinero en la cuenta")
        else:
            self.__dinero -= retiro
            print(f"se retiro el dinero exitosamente: {self.__dinero}")

    def __info_user(self):
        return print(f"nombre = {self.__nombre}, Numero de cuenta = {self.__n_cuenta},Saldo actual = {self.__dinero}, \nHistorial de cuenta = {}")

    def __equals__(self, other):
         return self.__n_cuenta == other.__n_cuenta
    def __str__(self):
         return f"Nombre: {self.__nombre}"


class Banco():
    def __init__(self):
        self.clientes = {

        }

    def new_client(self,cliente):
        if cliente.__n_cuenta in self.clientes:
            print("Numero de cuenta en uso")
        else:
            self.clientes[cliente.__n_cuenta] = cliente
    
    def Lista_clientes(self):
        for x in self.clientes.values():
            print(x)

cliente1 = Cliente("Juan", 2180021, 5000)
cliente2 = Cliente("esteban", 2180022, 5000)
banco = Banco()

cliente1.deposito(1000)
cliente1.retiro(6000)
print(cliente1 == cliente2)

banco.new_client(cliente1)
banco.new_client(cliente2)

banco.Lista_clientes()
