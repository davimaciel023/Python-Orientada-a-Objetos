# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def crescer(self):
        for i in range(21):
            self.__idade += 1
            print(20 * '=')
            print(f'Sua idade é {self.__idade}')
            self.__altura += 0.05
            print(f'Sua altura é {round(self.__altura, 2)}')
            self.__peso += 4
            print(f'Seu peso é {self.__peso}')
            print(20 * '=')

pessoa = Pessoa('Davi', 0, 9, 0.80)
pessoa.crescer()