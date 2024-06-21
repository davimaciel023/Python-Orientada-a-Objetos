# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def mostrar_cor(self):
        print(self.__cor)

bola = Bola('verde', 'redonda', 'couro')
bola.mostrar_cor()

bola = Bola('vermelha', 'redonda', 'couro')
bola.mostrar_cor()