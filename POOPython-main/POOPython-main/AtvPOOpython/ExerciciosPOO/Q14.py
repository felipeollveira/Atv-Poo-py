class ContaCorrente:
    def __init__(self, nomeConta, saldo):
        self.saldo = saldo
        self.nomeConta = nomeConta
        self.saldo = saldo
    def sacar(self, saque):
        if self.saldo < saque:
            print("Saldo insuficiente!")
        else:
            self.saldo -= saque     
    def depositar(self, deposito):
        self.saldo += deposito
    def mostar(self):
        print(f"O saldo da conta corrente {self.nomeConta} = {self.saldo}")


class ContaPoupanca:
    def __init__(self, nomeConta, saldo):
        self.saldo = saldo
        self.nomeConta = nomeConta
        self.saldo = saldo
    def sacar(self, saque):
        if self.saldo < saque:
            print("Saldo insuficiente!")
        else:
            self.saldo -= saque     
    def depositar(self, deposito):
        self.saldo += deposito
    def mostar(self):
        print(f"O saldo da conta poupança {self.nomeConta} = {self.saldo}")

nomeConta = input("Digite o nome da sua conta: ")
saldo = 0

contaCorrente1 = ContaCorrente(nomeConta, saldo)
contaPoupanca1 = ContaPoupanca(nomeConta, saldo)

op = 3

while op != 0:
    op = int(input("Digite 1 para acessar a conta corrente 2 para acessar a poupança e 0 para sair: "))
    if op == 1:
        opCorrente = 4
        while opCorrente != 0:
            opCorrente = int(input("Digite 1 para sacar 2 para depositar e 3 para ver o saldo e 0 para sair: "))
            if opCorrente == 1:
                saque = float(input("Digite o valor que deseja sacar: "))
                sacar1 = contaCorrente1.sacar(saque)
            elif opCorrente == 2:
                deposito = float(input("Digite o valor que deseja depositar: "))
                depositar1 = contaCorrente1.depositar(deposito)
            elif opCorrente == 3:
                mostrar1 = contaCorrente1.mostar()
    elif op == 2:
        opPoupanca = 4
        while opPoupanca != 0:
         opPoupanca = int(input("Digite 1 para sacar 2 para depositar e 3 para ver o saldo e 0 para sair: "))
        if opPoupanca == 1:
            saque = float(input("Digite o valor que deseja sacar: "))
            sacar1 = contaPoupanca1.sacar(saque)
        elif opPoupanca == 2:
            deposito = float(input("Digite o valor que deseja depositar: "))
            depositar1 = contaPoupanca1.depositar(deposito)
        elif opPoupanca == 3:
            mostrar1 = contaPoupanca1.mostar()