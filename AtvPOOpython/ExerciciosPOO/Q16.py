class FiguraGeometrica:
    def calcularArea(self):
        raise NotImplementedError("Este método deve ser sobrescrito.")

    def calcularPerimetro(self):
        raise NotImplementedError("Este método deve ser sobrescrito.")

class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2

    def calcularPerimetro(self):
        return 4 * self.lado

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return 3.14 * (self.raio ** 2)

    def calcularPerimetro(self):
        return 2 * 3.14 * self.raio

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularPerimetro(self):
        return self.lado1 + self.lado2 + self.lado3

if __name__ == "__main__":
    print("Escolha a figura geométrica:")
    print("[1] Quadrado")
    print("[2] Círculo")
    print("[3] Triângulo")
    
    escolha = int(input("Digite o número correspondente à figura desejada: "))

    if escolha == 1:
        lado = float(input("Digite o valor do lado do quadrado: "))
        quadrado = Quadrado(lado)
        print(f"Área do quadrado: {quadrado.calcularArea()}")
        print(f"Perímetro do quadrado: {quadrado.calcularPerimetro()}")
    
    elif escolha == 2:
        raio = float(input("Digite o valor do raio do círculo: "))
        circulo = Circulo(raio)
        print(f"\nÁrea do círculo: {circulo.calcularArea():.2f}")
        print(f"Perímetro do círculo: {circulo.calcularPerimetro():.2f}")
    
    elif escolha == 3:
        base = float(input("Digite o valor da base do triângulo: "))
        altura = float(input("Digite o valor da altura do triângulo: "))
        lado1 = float(input("Digite o valor do lado 1 do triângulo: "))
        lado2 = float(input("Digite o valor do lado 2 do triângulo: "))
        lado3 = float(input("Digite o valor do lado 3 do triângulo: "))
        triangulo = Triangulo(base, altura, lado1, lado2, lado3)
        print(f"\nÁrea do triângulo: {triangulo.calcularArea()}")
        print(f"Perímetro do triângulo: {triangulo.calcularPerimetro()}")
    
    else:
        print("Opção inválida!")
