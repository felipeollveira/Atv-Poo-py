import random

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    naipes = ["Copas", "Ouros", "Espadas", "Paus"]

    def __init__(self):
        self.cartas = [Carta(valor, naipe) for valor in Baralho.valores for naipe in Baralho.naipes]

    def embaralhar(self):
        random.shuffle(self.cartas)
        print("Baralho embaralhado!")

    def distribuirCarta(self):
        return self.cartas.pop() if self.cartas else None

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receberCarta(self, carta):
        if carta:
            self.mao.append(carta)

    def mostrarMao(self):
        if self.mao:
            print(f"{self.nome} tem as seguintes cartas:")
            for carta in self.mao:
                print(f"- {carta}")
        else:
            print(f"{self.nome} ainda não tem cartas.")

def jogo():
    baralho = Baralho()
    baralho.embaralhar()

    jogador1 = Jogador("Jogador 1")
    jogador2 = Jogador("Jogador 2")

    for _ in range(5):
        jogador1.receberCarta(baralho.distribuirCarta())
        jogador2.receberCarta(baralho.distribuirCarta())

    jogador1.mostrarMao()
    print()
    jogador2.mostrarMao()

jogo()
