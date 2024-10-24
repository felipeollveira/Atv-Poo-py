"""
questão 36 pede pra aprimorar a classe anterior
com o metodo aumentarSalario por porcentagem
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self): 
        return self.nome
    
    def obter_salario(self): 
        return self.salario
    
    def aumentarSalario(self, newSalario):
        self.salario = self.salario + ((newSalario/100) * self.salario)

nome_funcionario = input("Digite o nome do funcionário: ")
salario = int(input("Digite o salário do funcionário: "))

fun1 = Funcionario(nome_funcionario, salario)

print(fun1.obter_nome())  
print(fun1.obter_salario()) 

fun1.aumentarSalario(10)
print(fun1.obter_salario()) 
