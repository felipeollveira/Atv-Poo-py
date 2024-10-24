class Atleta:
    def __init__(self, aposentado=False, peso=0):
        self.aposentado = aposentado
        self.peso = peso

    def aposentar(self):
        self.aposentado = True

    def aquecer(self):
        print("Aquecendo...")


class Corredor(Atleta):
    def correr(self):
        print("Correndo...")


class Nadador(Atleta):
    def nadar(self):
        print("Nadando...")


class Ciclista(Atleta):
    def pedalar(self):
        print("Pedalando...")


class TriAtleta(Corredor, Nadador, Ciclista):  # Herança múltipla
    pass  
