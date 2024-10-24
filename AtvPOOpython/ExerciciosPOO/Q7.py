class Aluno():
    def __init__(self, nome, matricula, disciplina, nota):
        self.nome = nome 
        self.matricula = matricula 
        self.nota = nota 
        self.disciplina = disciplina

    def media(self):
        total_notas = sum(self.nota) 
        return total_notas / len(self.nota)  

nome = input("Digite seu nome: ")  
matricula = input("Digite sua matricula: ")
disciplina = input("Digite a disciplina: ")

contador = ""
notas = []

while contador != "N":
    nota = float(input("Digite sua nota: "))
    notas.append(nota) 

    contador = input("Deseja adicionar mais alguma nota? [Y/N]: ").upper()


aluno1 = Aluno(nome, matricula, disciplina, notas) 

media1 = aluno1.media()
print(f"Sua média é {media1}")  
