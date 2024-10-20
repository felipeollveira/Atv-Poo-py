class ContaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
    
    def alterarNome(self, novoNome):
        self.nomeCorrentista = novoNome
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def saque(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")
    
    def mostrarSaldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
    
    def mostrarDetalhes(self):
        print(f"Número da conta: {self.numeroConta}")
        print(f"Nome do correntista: {self.nomeCorrentista}")
        self.mostrarSaldo()

numeroConta = input("Insira o número da conta: ")
nomeCorrentista = input("Insira o nome do correntista: ")

conta = ContaCorrente(numeroConta, nomeCorrentista)

conta.mostrarDetalhes()

novoNome = input("Deseja alterar o nome do correntista? (Digite o novo nome ou deixe em branco para manter): ")
if novoNome:
    conta.alterarNome(novoNome)

valorDeposito = float(input("Insira o valor a ser depositado: "))
conta.deposito(valorDeposito)

valorSaque = float(input("Insira o valor a ser sacado: "))
conta.saque(valorSaque)

print("\nDetalhes finais da conta:")
conta.mostrarDetalhes()
