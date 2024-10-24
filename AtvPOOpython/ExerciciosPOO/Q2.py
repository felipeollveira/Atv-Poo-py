class ContaBancaria():

    def __init__(self, saldo, numero_de_conta):
        self.saldo = saldo
        self.numero_de_conta = numero_de_conta

    def depositar(self,valor):
        self.saldo += valor
        return self.saldo

    def sacar(self,valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
        return self.saldo
    
