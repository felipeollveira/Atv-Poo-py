class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def obter_nome(self):
        return self.__nome
    
    def obter_salario(self):
        return self.__salario
    
    def alterar_salario(self, novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario
        else:
            print("Erro: O salario deve ser maior que zero.")

            funcionario1 = Funcionario("João", 5000)

            print("Nome:",funcionario1.obter_nome)
            print("Salário:",funcionario1.obter_salario)

            funcionario1.alterar_salario(5500)
            print("Novo salário:", funcionario1.obter_salario())

            funcionario1.alterar_salario(-1000)