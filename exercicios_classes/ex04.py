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
        for i in (self.__idade - 21):
            if self.__idade < 21:
                self.__altura += 0.05
                print(self.__altura)
            else:
                ...
pessoa = Pessoa('Davi', 17, '80kg', 1.83)
pessoa.crescer()