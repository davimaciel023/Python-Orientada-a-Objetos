"""
Métodos de classes + factories(fábricas)
são métodos onde 'self' será 'cls', ou seja,
ao invés de receber a instância no primeiro
parâmetro, receberemos a própria classe.
"""
class Pessoa:
    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
   
    @classmethod
    def criar_50_anos(cls, nome):
        return cls(nome, 50)

p1 = Pessoa('davi', 17)
p2 = Pessoa.criar_50_anos('Nagilla')
Pessoa.metodo_de_classe()
print(p2.nome, p2.idade)