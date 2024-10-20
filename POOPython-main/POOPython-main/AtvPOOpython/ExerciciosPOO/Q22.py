class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.__notas = []  
    
    def adicionarNota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida. Insira uma nota entre 0 e 10.")
    
    def calcularMedia(self):
        if len(self.__notas) == 0:
            return 0  
        return sum(self.__notas) / len(self.__notas)
    
    def obterNotas(self):
        return self.__notas.copy() 
    

    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Média: {self.calcularMedia():.2f}")

def inserirNotas(aluno):
    while True:
        try:
            nota = float(input("Insira uma nota (ou -1 para sair): "))
            if nota == -1:
                break
            aluno.adicionarNota(nota)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

nome = input("Insira o nome do aluno: ")
matricula = input("Insira a matrícula do aluno: ")

aluno1 = Aluno(nome, matricula)
inserirNotas(aluno1)

aluno1.mostrar()
