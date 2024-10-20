class Circulo():
    def __init__(self,raio):
        self.raio = raio
    
    def area(self):
        return self.raio * 3.14
    
    def perimetro(self):
        return self.raio * 3.14 * 2
    
raio = float(input("Digite o raio do circulo: "))
circulo1 = Circulo(raio)
area = circulo1.area()

print(f"A area é: {area}")

perimetro = circulo1.perimetro()
print(f"O perimetro é: {perimetro}")