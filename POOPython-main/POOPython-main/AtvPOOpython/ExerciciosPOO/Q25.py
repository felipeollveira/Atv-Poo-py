class Quadrado:
    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado
    
    def mudarValorLado(self, novoLado):
        if novoLado > 0:
            self.tamanhoLado = novoLado
        else:
            print("O valor do lado deve ser positivo.")
    
    def retornarValorLado(self):
        return self.tamanhoLado
    
    def calcularArea(self):
        return self.tamanhoLado ** 2

def solicitarValores():
    while True:
        try:
            tamanhoLado = float(input("Insira o tamanho do lado do quadrado: "))
            if tamanhoLado > 0:
                return tamanhoLado
            else:
                print("O valor deve ser positivo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

lado = solicitarValores()
quadrado = Quadrado(lado)

print(f"O valor do lado do quadrado é: {quadrado.retornarValorLado()}")
print(f"A área do quadrado é: {quadrado.calcularArea()}")

novoLado = solicitarValores()
quadrado.mudarValorLado(novoLado)

print(f"Novo valor do lado: {quadrado.retornarValorLado()}")
print(f"Nova área do quadrado: {quadrado.calcularArea()}")
