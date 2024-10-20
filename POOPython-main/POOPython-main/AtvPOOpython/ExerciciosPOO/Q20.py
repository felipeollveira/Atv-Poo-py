# Classe base Produto
class Produto:
    def __init__(self, titulo, preco):
        self.__titulo = titulo
        self.__preco = preco

    def mostrarDetalhes(self):
        return f"Título: {self.__titulo}\nPreço: R${self.__preco:.2f}"

# Classe Livro que herda de Produto
class Livro(Produto):
    def __init__(self, titulo, preco, autor, numero_paginas):
        super().__init__(titulo, preco)
        self.__autor = autor
        self.__numero_paginas = numero_paginas

    def mostrarDetalhes(self):
        detalhes = super().mostrarDetalhes()
        return f"{detalhes}\nAutor: {self.__autor}\nNúmero de Páginas: {self.__numero_paginas}"


class Ebook(Produto):
    def __init__(self, titulo, preco, tamanho_arquivo):
        super().__init__(titulo, preco)
        self.__tamanho_arquivo = tamanho_arquivo

    def mostrarDetalhes(self):
        detalhes = super().mostrarDetalhes()
        return f"{detalhes}\nTamanho do Arquivo: {self.__tamanho_arquivo} MB"

class Audiolivro(Produto):
    def __init__(self, titulo, preco, duracao):
        super().__init__(titulo, preco)
        self.__duracao = duracao

    def mostrarDetalhes(self):
        detalhes = super().mostrarDetalhes()
        return f"{detalhes}\nDuração: {self.__duracao} horas"

def criarLivro():
    titulo = input("Digite o título do livro: ")
    preco = float(input("Digite o preço do livro: R$ "))
    autor = input("Digite o autor do livro: ")
    numero_paginas = int(input("Digite o número de páginas: "))
    return Livro(titulo, preco, autor, numero_paginas)

def criarEbook():
    titulo = input("Digite o título do ebook: ")
    preco = float(input("Digite o preço do ebook: R$ "))
    tamanho_arquivo = float(input("Digite o tamanho do arquivo (em MB): "))
    return Ebook(titulo, preco, tamanho_arquivo)

def criarAudiolivro():
    titulo = input("Digite o título do audiolivro: ")
    preco = float(input("Digite o preço do audiolivro: R$ "))
    duracao = float(input("Digite a duração do audiolivro (em horas): "))
    return Audiolivro(titulo, preco, duracao)


print("Cadastrar um Livro:")
livro = criarLivro()
print("\nDetalhes do Livro:")
print(livro.mostrarDetalhes())

print("\nCadastrar um Ebook:")
ebook = criarEbook()
print("\nDetalhes do Ebook:")
print(ebook.mostrarDetalhes())

print("\nCadastrar um Audiolivro:")
audiolivro = criarAudiolivro()
print("\nDetalhes do Audiolivro:")
print(audiolivro.mostrarDetalhes())
