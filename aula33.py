# Funções decoradoras e decoradores com vlasses
def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls

@adiciona_repr    
class Time:
    def __init__(self, nome):
        self.nome = nome
    
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    def falar_nome(self):
        return f'O planeta é {self.nome}'

brasil = Time('brasil')
portugal = Time('portugal')

terra = Planeta('terra')
marte = Planeta('marte')

print(brasil)
print(portugal)
print(terra)
print(marte)
print(terra.falar_nome())
print(marte.falar_nome())