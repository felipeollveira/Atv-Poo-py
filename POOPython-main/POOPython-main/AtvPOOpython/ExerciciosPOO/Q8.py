class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcularSalario():
        if cargo == 1:
            return salario * 1.03
        elif cargo == 2:
            return salario * 1.05
        elif cargo == 3:
            return salario

nome = input("Digite seu nome")
salario = input("Digite seu salário")
cargo = input("digite: \n[1]: Coordenador\n[2]: Gerente \n[3]: Presidente")
    