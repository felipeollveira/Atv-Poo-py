class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def mudarValorLados(self, novoComprimento, novaLargura):
        if novoComprimento > 0 and novaLargura > 0:
            self.comprimento = novoComprimento
            self.largura = novaLargura
        else:
            print("Os valores devem ser positivos.")
    
    def retornarValorLados(self):
        return self.comprimento, self.largura
    
    def calcularArea(self):
        return self.comprimento * self.largura
    
    def calcularPerimetro(self):
        return 2 * (self.comprimento + self.largura)

def solicitarMedidas():
    while True:
        try:
            comprimento = float(input("Insira o comprimento do local (em metros): "))
            largura = float(input("Insira a largura do local (em metros): "))
            if comprimento > 0 and largura > 0:
                return comprimento, largura
            else:
                print("Os valores devem ser positivos. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def calcularPisosERodapes(retangulo, areaPiso, comprimentoRodape):
    areaLocal = retangulo.calcularArea()
    perimetroLocal = retangulo.calcularPerimetro()
    
    quantidadePisos = areaLocal / areaPiso
    quantidadeRodape = perimetroLocal / comprimentoRodape
    
    return quantidadePisos, quantidadeRodape

comprimento, largura = solicitarMedidas()
retanguloLocal = Retangulo(comprimento, largura)


areaPiso = 0.36
comprimentoRodape = 2.5

quantidadePisos, quantidadeRodape = calcularPisosERodapes(retanguloLocal, areaPiso, comprimentoRodape)

print(f"\nPara o local de {retanguloLocal.calcularArea():.2f} m²:")
print(f"Quantidade de pisos necessária: {quantidadePisos:.2f} unidades")
print(f"Quantidade de rodapés necessária: {quantidadeRodape:.2f} metros")
