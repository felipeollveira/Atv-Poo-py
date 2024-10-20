class TV:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume
    
    def mudarCanal(self, novoCanal):
        if 1 <= novoCanal <= 99:
            self.canal = novoCanal
            print(f"Canal alterado para {self.canal}.")
        else:
            print("Canal inválido! Insira um canal entre 1 e 99.")
    
    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume: {self.volume}")
        else:
            print("Volume máximo atingido.")
    
    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume: {self.volume}")
        else:
            print("Volume mínimo atingido.")
    
    def mostrarStatus(self):
        print(f"Canal atual: {self.canal}, Volume atual: {self.volume}")

tv = TV()

while True:
    print("\nOpções:")
    print("1 - Mudar canal")
    print("2 - Aumentar volume")
    print("3 - Diminuir volume")
    print("4 - Mostrar status da TV")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            novoCanal = int(input("Insira o número do canal (1 a 99): "))
            tv.mudarCanal(novoCanal)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")
    
    elif opcao == "2":
        tv.aumentarVolume()
    
    elif opcao == "3":
        tv.diminuirVolume()
    
    elif opcao == "4":
        tv.mostrarStatus()
    
    elif opcao == "5":
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida! Escolha uma das opções disponíveis.")
