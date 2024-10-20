class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mover(self):
        pass
    
    def emitirSom(self):
        pass
    
    def mostrar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

class Mamifero(Animal):
    def __init__(self, nome, idade, temPelo):
        super().__init__(nome, idade)
        self.temPelo = temPelo
    
    def mover(self):
        print(f"{self.nome} está correndo.")
    
    def emitirSom(self):
        print(f"{self.nome} está emitindo um som de mamífero.")
    
    def mostrar(self):
        super().mostrar()
        print(f"Tem pelo: {'Sim' if self.temPelo else 'Não'}")

class Ave(Animal):
    def __init__(self, nome, idade, podeVoar):
        super().__init__(nome, idade)
        self.podeVoar = podeVoar
    
    def mover(self):
        if self.podeVoar:
            print(f"{self.nome} está voando.")
        else:
            print(f"{self.nome} está caminhando.")
    
    def emitirSom(self):
        print(f"{self.nome} está cantando.")
    
    def mostrar(self):
        super().mostrar()
        print(f"Pode voar: {'Sim' if self.podeVoar else 'Não'}")

class Peixe(Animal):
    def __init__(self, nome, idade, viveEmAguaSalgada):
        super().__init__(nome, idade)
        self.viveEmAguaSalgada = viveEmAguaSalgada
    
    def mover(self):
        print(f"{self.nome} está nadando.")
    
    def emitirSom(self):
        print(f"{self.nome} não emite som perceptível.")
    
    def mostrar(self):
        super().mostrar()
        print(f"Vive em água salgada: {'Sim' if self.viveEmAguaSalgada else 'Não'}")

# Exemplo de uso:
mamifero = Mamifero("Elefante", 10, True)
ave = Ave("Papagaio", 2, True)
peixe = Peixe("Tubarão", 5, True)

mamifero.mostrar()
mamifero.mover()
mamifero.emitirSom()

print("\n")

ave.mostrar()
ave.mover()
ave.emitirSom()

print("\n")

peixe.mostrar()
peixe.mover()
peixe.emitirSom()
