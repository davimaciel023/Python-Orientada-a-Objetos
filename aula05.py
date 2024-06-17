# Atributos de classes
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('davi', 17)
p2 = Pessoa('nagilla', 18)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())