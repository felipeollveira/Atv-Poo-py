# Classe base Publicacao
class Publicacao:
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
    
    # Método para mostrar detalhes da publicação (a ser sobrescrito nas subclasses)
    def mostrarDetalhes(self):
        pass
    
    # Método para mostrar conteúdo (a ser sobrescrito nas subclasses)
    def mostrarConteudo(self):
        pass

# Classe Livro que herda de Publicacao
class Livro(Publicacao):
    def __init__(self, titulo, autor, anoPublicacao, numPaginas):
        super().__init__(titulo, autor, anoPublicacao)
        self.numPaginas = numPaginas
        self.conteudo = "Conteúdo do livro"  # Conteúdo protegido, acessível apenas pela classe
    
    def mostrarDetalhes(self):
        print(f"Livro: {self.titulo}\nAutor: {self.autor}\nAno: {self.anoPublicacao}\nPáginas: {self.numPaginas}")
    
    def mostrarConteudo(self):
        print(f"Conteúdo do Livro: {self.conteudo}")

# Classe Revista que herda de Publicacao
class Revista(Publicacao):
    def __init__(self, titulo, autor, anoPublicacao, edicao):
        super().__init__(titulo, autor, anoPublicacao)
        self.edicao = edicao
        self.conteudo = "Conteúdo da revista"  # Conteúdo protegido
    
    def mostrarDetalhes(self):
        print(f"Revista: {self.titulo}\nAutor: {self.autor}\nAno: {self.anoPublicacao}\nEdição: {self.edicao}")
    
    def mostrarConteudo(self):
        print(f"Conteúdo da Revista: {self.conteudo}")


class Artigo(Publicacao):
    def __init__(self, titulo, autor, anoPublicacao, revistaPublicacao):
        super().__init__(titulo, autor, anoPublicacao)
        self.revistaPublicacao = revistaPublicacao
        self.conteudo = "Conteúdo do artigo" 
    
    def mostrarDetalhes(self):
        print(f"Artigo: {self.titulo}\nAutor: {self.autor}\nAno: {self.anoPublicacao}\nPublicado na Revista: {self.revistaPublicacao}")
    
    def mostrarConteudo(self):
        print(f"Conteúdo do Artigo: {self.conteudo}")


livro = Livro("Teste ", "Testoncio ", 1978, 1)
revista = Revista("Exemplo", "Exemplino", 1578, "Edição 1")
artigo = Artigo("Programando ", "Rafael ", 2024, "Eu")


livro.mostrarDetalhes()
livro.mostrarConteudo()

print("\n")

revista.mostrarDetalhes()
revista.mostrarConteudo()

print("\n")

artigo.mostrarDetalhes()
artigo.mostrarConteudo()
