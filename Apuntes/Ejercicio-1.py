

class Cliente():
    def __init__(self, nombre, n_cuenta, dinero):
        self.nombre = nombre
        self.n_cuenta = n_cuenta
        self.dinero = dinero

    
    def deposito(self,new_deposito):
        self.dinero += new_deposito
        print(f"Dinero actual en la cuenta: {self.dinero}")
    
    def retiro(self, retiro):
        if retiro > self.dinero:
            print("El retiro es mayor al dinero en la cuenta")
            print(f"el dinero actual en la cuenta es: {self.dinero}")
        else:
            self.dinero -= retiro
            print(f"Dinero actual en la cuenta: {self.dinero}")

    def __equals__(self, other):
         return self.n_cuenta == other.n_cuenta
    def __str__(self):
         return f"Nombre: {self.nombre} \nNumero de cuenta: {self.n_cuenta} \nDinero: {self.dinero}"
class Banco():
    def __init__(self):
        self.clientes = {

        }

    def new_client(self,cliente):
        if cliente.n_cuenta in self.clientes:
            print("Numero de cuenta en uso")
        else:
            self.clientes[cliente.n_cuenta] = cliente
    
    def Lista_clientes(self):
        for x in self.clientes.values():
            print(x)

cliente1 = Cliente("Juan", n_cuenta=2180021, dinero=5000)
cliente2 = Cliente("esteban", n_cuenta=2180022, dinero=5000)
banco = Banco()

cliente1.deposito(1000)
cliente1.retiro(6000)
print(cliente1 == cliente2)

banco.new_client(cliente1)
banco.new_client(cliente2)

banco.Lista_clientes()
