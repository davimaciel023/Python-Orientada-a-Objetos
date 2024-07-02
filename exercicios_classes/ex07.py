"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""
class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, nome):
        self.nome = nome
        print(f'Seu novo nome é {self.nome}')
    
    def alterar_fome(self, fome):
        self.fome = fome
        print(f'Sua nova fome é {self.fome}')

    def alterar_saude(self, saude):
        self.saude = saude
        print(f'Sua saude é {self.saude}')

    def alterar_idade(self, idade):
        self.idade = idade
        print(f'Sua idade é {self.idade}')

    def CheckHumor(self):
        if self.fome >= 7 or self.saude <= 3:
            print('Está Mal humorado')
        else:
            print("Está bem humorado")


dog = BichinhoVirtual('Dog', 6, 4, 3)
dog.alterar_nome('feroz')
dog.alterar_fome(7)
dog.alterar_idade(4)
dog.alterar_saude(5)
dog.CheckHumor()