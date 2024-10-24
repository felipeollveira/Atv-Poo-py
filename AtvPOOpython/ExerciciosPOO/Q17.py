import time
import os

class Veiculo:
    def _init_(self, velocidadeMaxima):
        self.velocidadeAtual = 0
        self.velocidadeMaxima = velocidadeMaxima

    def acelerar(self, acelerando):
        self.velocidadeAtual += acelerando
        if self.velocidadeAtual > self.velocidadeMaxima:
            self.velocidadeAtual = self.velocidadeMaxima
        print(f"Acelerando!\nVelocidade atual: {self.velocidadeAtual} km/h")
        time.sleep(2)  

    def frear(self, freiando):
        self.velocidadeAtual -= freiando
        if self.velocidadeAtual < 0:
            self.velocidadeAtual = 0
        print(f"Freiando!\nVelocidade atual: {self.velocidadeAtual} km/h")
        time.sleep(2)  

class Carro(Veiculo):
    def _init_(self):
        super()._init_(velocidadeMaxima=300)

class Moto(Veiculo):
    def _init_(self):
        super()._init_(velocidadeMaxima=150)

class Bicicleta(Veiculo):
    def _init_(self):
        super()._init_(velocidadeMaxima=45)


op = input("Digite o número correspondente para controlar o veículo desejado:\n[1] Carro\n[2] Moto\n[3] Bicicleta\n")

if op == "1":
    veiculo = Carro()
    print("Você escolheu o Carro!")
elif op == "2":
    veiculo = Moto()
    print("Você escolheu a Moto!")
elif op == "3":
    veiculo = Bicicleta()
    print("Você escolheu a Bicicleta!")
else:
    print("Opção inválida.")
    veiculo = None

if veiculo:
    while True:
        acao = input("\nDigite o número correspondente para executar a ação desejada:\n[1] Acelerar\n[2] Frear\n[3] Limpar Tela\n[4] Sair\n")

        if acao == "1":
            incremento = int(input("Digite o valor para acelerar (km/h): "))
            veiculo.acelerar(incremento)
        elif acao == "2":
            decremento = int(input("Digite o valor para frear (km/h): "))
            veiculo.frear(decremento)
        elif acao == "3":
            os.system('cls' if os.name == 'nt' else 'clear')  
        elif acao == "4":
            for _ in range(3):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Saindo" + "." * (_ + 1))
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saída concluída.")
            break
        else:
            print("Opção inválida, tente novamente.")