class Animal:
    def emitir_som(self):
        raise NotImplementedError("Este método deve ser sobrescrito na classe derivada.")

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"


class Gato(Animal):
    def emitir_som(self):
        return "Miau!"


class Peixe(Animal):
    def emitir_som(self):
        return "Glub Glub!"


def fazer_animais_emitir_som(animais):
    for animal in animais:
        print(animal.emitir_som())


cachorro = Cachorro()
gato = Gato()
peixe = Peixe()


lista_animais = [cachorro, gato, peixe]


fazer_animais_emitir_som(lista_animais)
