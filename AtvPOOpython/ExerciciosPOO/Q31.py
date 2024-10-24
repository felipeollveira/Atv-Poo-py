class Macaco:
    def __init__(self, nome):
       
        self.nome = nome
        self.bucho = []  

    def comer(self, alimento):
       
        if isinstance(alimento, Macaco): 
            print(f"{self.nome} não pode comer a si mesmo!")
            return
        
        if isinstance(alimento, Macaco) and alimento is not self:
            self.bucho.append(alimento.nome) 
            print(f"{self.nome} comeu {alimento.nome}!")
        elif isinstance(alimento, str):
            self.bucho.append(alimento)
            print(f"{self.nome} comeu {alimento}!")
        else:
            print(f"{self.nome} tentou comer algo estranho e não conseguiu!")

    def ver_bucho(self):
        if self.bucho: 
            print(f"Bucho de {self.nome}: {', '.join(self.bucho)}")
        else:
            print(f"O bucho de {self.nome} está vazio")

    def digerir(self):
        if self.bucho:
            digerido = self.bucho.pop(0)  
            print(f"{self.nome} digeriu {digerido}")
        else:
            print(f"{self.nome} não tem nada para digerir!")


macaco1 = Macaco("Carlos")
macaco2 = Macaco("George")

# comidas
macaco1.comer("banana")
macaco1.ver_bucho()
macaco1.comer("maçã")
macaco1.ver_bucho()
macaco1.comer("manga")
macaco1.ver_bucho()

macaco2.comer("uva")
macaco2.ver_bucho()
macaco2.comer("pera")
macaco2.ver_bucho()
macaco2.comer("melancia")
macaco2.ver_bucho()


macaco1.comer(macaco2)
macaco1.ver_bucho()

macaco1.comer(macaco1) 
macaco1.ver_bucho()



# Digerindo alguns alimentos
macaco1.digerir()
macaco1.ver_bucho()
macaco2.digerir()
macaco2.ver_bucho()


