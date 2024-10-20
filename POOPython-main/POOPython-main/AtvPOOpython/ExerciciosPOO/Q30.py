class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude 
        self.idade = idade
    
    def alterarNome(self, novoNome):
        self.nome = novoNome
    
    def alterarFome(self, novaFome):
        if 0 <= novaFome <= 10:
            self.fome = novaFome
        else:
            print("O valor da fome deve ser entre 0 e 10.")
    
    def alterarSaude(self, novaSaude):
        if 0 <= novaSaude <= 10:
            self.saude = novaSaude
        else:
            print("O valor da saúde deve ser entre 0 e 10.")
    

    def alterarIdade(self, novaIdade):
        if novaIdade >= 0:
            self.idade = novaIdade
        else:
            print("A idade deve ser um valor positivo.")
    
    def retornarNome(self):
        return self.nome
    
    def retornarFome(self):
        return self.fome
    
    def retornarSaude(self):
        return self.saude
    
    def retornarIdade(self):
        return self.idade
    
    def calcularHumor(self):
        humor = (self.saude + (10 - self.fome)) / 2
        return humor
    
    def mostrarStatus(self):
        print(f"Nome: {self.nome}")
        print(f"Fome: {self.fome}/10")
        print(f"Saúde: {self.saude}/10")
        print(f"Idade: {self.idade} anos")
        print(f"Humor: {self.calcularHumor():.2f}/10")

bichinho = Tamagushi("Tama", 5, 8, 2)

bichinho.mostrarStatus()

bichinho.alterarFome(3)
bichinho.alterarSaude(9)
bichinho.alterarIdade(3)

print("\nApós as alterações:")
bichinho.mostrarStatus()
