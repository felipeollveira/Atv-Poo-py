class Produto:
    def __init__(self, preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade
    
    def mostrar(self):
        print(f"Preço do produto: R$ {self.preco}\nQuantidade: {self.quantidade}")

class Eletronico(Produto):
    def __init__(self, preco, quantidade, marca, modelo):
        super().__init__(preco, quantidade)
        self.marca = marca
        self.modelo = modelo
    
    def mostrarDetalhes(self):
        super().mostrar()
        print(f"Marca: {self.marca}\nModelo: {self.modelo}")

class Roupa(Produto):
    def __init__(self, preco, quantidade, tamanho, material):
        super().__init__(preco, quantidade)
        self.tamanho = tamanho
        self.material = material

    def mostrarDetalhes(self):
        super().mostrar()
        print(f"Tamanho: {self.tamanho}\nMaterial: {self.material}")

op = int(input("Digite 1 para escolher um eletrônico e 2 para roupa: "))
preco = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

if op == 1:
    marca = input("Digite a marca desejada: ")
    modelo = input("Digite o modelo desejado: ")
    eletronico = Eletronico(preco, quantidade, marca, modelo)
    eletronico.mostrarDetalhes()

elif op == 2:
    tamanho = input("Digite o tamanho desejado: ")
    material = input("Digite o material desejado: ")
    roupa = Roupa(preco, quantidade, tamanho, material)
    roupa.mostrarDetalhes()

else:
    print("Opção inválida!")
