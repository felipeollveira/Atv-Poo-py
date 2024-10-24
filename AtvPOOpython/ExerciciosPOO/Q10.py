class Veiculo:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self, estado):
        if estado == "parado":
            estado = "andando"
            print("Acelerando!")
        else:
            print("O carro já está andando!")
        return estado 
    
    def freiar(self, estado):
        if estado == "andando":
            estado = "parado"
            print("Freiando o carro!")
        else:
            print("O carro já está parado!")
        return estado  


cor = input("Digite a cor do seu carro: ")
marca = input("Digite a marca do seu carro: ")
modelo = input("Digite o modelo do seu carro: ")

estado = "parado"

veiculo1 = Veiculo(cor, marca, modelo)

op = 1


while op != 0:
    op = int(input("Digite 1 para acelerar, 2 para freiar, e 0 para sair: "))
    if op == 1:
        estado = veiculo1.acelerar(estado)  # Atualiza o estado
    elif op == 2:
        estado = veiculo1.freiar(estado)    # Atualiza o estado


