class Bola():
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def trocarCor(self):
        self.cor = input("Digite uma cor: ")

    def mostrarCor(self):
        return f"Cor: {self.cor}"
    

bola1 = Bola("laranja", 5, "borracha")

trocar = bola1.trocarCor()

mostrar = bola1.mostrarCor()
print(mostrar)