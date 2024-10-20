class Produto():

    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque
    
    def atualizar_estoque(self,valor):
       if self.quantidade_em_estoque - valor < 0:
        print("Estoque insuficiente para essa operação")
       else:
          self.quantidade_em_estoque -= valor


