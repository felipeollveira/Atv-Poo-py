
class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        if self.combustivel * self.consumo >= distancia:
            self.combustivel -= distancia / self.consumo
        else:
            print(f"Combustível insuficiente para essa distancia. {(distancia,self.combustivel)}")

    def obterGasolina(self):
        return f"Gasolina no tanque: {self.combustivel}"

    def adicionarGasolina(self, quantidade):
        print(f"Add gasolina: {quantidade}")
        self.combustivel += quantidade


meuFusca = Carro(15)  
meuFusca.adicionarGasolina(20)  
meuFusca.andar(100) 
print(meuFusca.obterGasolina()) 

meuFusca.andar(200)  
print(meuFusca.obterGasolina())
meuFusca.adicionarGasolina(10)
print(meuFusca.obterGasolina())
