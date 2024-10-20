class Pessoa():

    def __init__(self, nome, idade, cidade):
        self.nome = nome 
        self.idade = idade
        self.cidade = cidade

    def mostrar(self):
        return f"Nome: {self.nome} Idade: {self.idade} Cidade: {self.cidade}"


nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ") 
cidade = input("Digite sua cidade: ")

pessoa1 = Pessoa(nome,idade,cidade)

mensagem = pessoa1.mostrar()
print(mensagem)