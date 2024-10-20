class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario
        self.__cargo = cargo

    def getNome(self):
        return self.__nome

    def getSalario(self):
        return self.__salario

    def getCargo(self):
        return self.__cargo

    def setNome(self, nome):
        self.__nome = nome

    def setSalario(self, salario):
        self.__salario = salario


    def setCargo(self, cargo):
        self.__cargo = cargo

    def exibirInformacoes(self):
        print(f"Nome: {self.__nome}, Salário: R${self.__salario}, Cargo: {self.__cargo}")

def criarFuncionario():
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    cargo = input("Digite o cargo do funcionário: ")

    return Funcionario(nome, salario, cargo)


funcionario = criarFuncionario()

funcionario.exibirInformacoes()

novo_salario = float(input("\nDigite o novo salário (ou o mesmo valor para manter): "))
funcionario.setSalario(novo_salario)

novo_cargo = input("Digite o novo cargo (ou o mesmo cargo para manter): ")
funcionario.setCargo(novo_cargo)

funcionario.exibirInformacoes()
