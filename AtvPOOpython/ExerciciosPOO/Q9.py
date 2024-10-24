class Livro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
    
    def mostrar(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nNúmero de páginas: {self.numero_paginas}")
    

titulo = input("Digite o título do livro desejado: ")
autor = input("Digite o nome do autor: ")
numero_paginas = input("Digite o numero de páginas: ")

livro1 = Livro(titulo, autor, numero_paginas)
mostar1 = livro1.mostrar()
