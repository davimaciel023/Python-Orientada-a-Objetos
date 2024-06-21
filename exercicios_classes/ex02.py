# Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
class Quadrado:
    def __init__(self, tamanho):
        self.__tamanho = tamanho

    def valor_lado(self):
        return f'O valor do lado é {self.__tamanho} e a Área dele é {self.__tamanho * 2}'

quadrado = Quadrado(12.3)
print(quadrado.valor_lado())