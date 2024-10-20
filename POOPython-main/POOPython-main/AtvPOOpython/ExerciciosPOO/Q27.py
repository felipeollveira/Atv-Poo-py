class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    

    def envelhecer(self, anos):
        for _ in range(anos):
            if self.idade < 21:
                self.crescer(0.5)
            self.idade += 1
    
    def engordar(self, quilos):
        self.peso += quilos
    
    def emagrecer(self, quilos):
        if quilos <= self.peso:
            self.peso -= quilos
        else:
            print("Não é possível emagrecer mais do que o peso atual.")
    

    def crescer(self, centimetros):
        self.altura += centimetros / 100
    
    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso:.2f} kg")
        print(f"Altura: {self.altura:.2f} metros")

def solicitarAnos():
    while True:
        try:
            anos = int(input("Quantos anos deseja envelhecer? "))
            if anos > 0:
                return anos
            else:
                print("O número de anos deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

nome = input("Insira o nome da pessoa: ")
idade = int(input("Insira a idade da pessoa: "))
peso = float(input("Insira o peso da pessoa (em kg): "))
altura = float(input("Insira a altura da pessoa (em metros): "))

pessoa = Pessoa(nome, idade, peso, altura)
pessoa.mostrar()

anos = solicitarAnos()
pessoa.envelhecer(anos)

pessoa.engordar(5)

print("\nDetalhes após envelhecer e engordar:")
pessoa.mostrar()
