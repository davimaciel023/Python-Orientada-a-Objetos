# Classe Retangulo: Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
import os
class Retangulo:
    os.system('cls')
    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura

    def mudar_valores(self):
        area = self.__largura * self.__comprimento
        perimetro = 2 * (self.__comprimento + self.__largura)
        print()
        return f'{20 * '='}\n Os valores do retangulo são: \n {self.__largura} de largura \n {self.__comprimento} de comprimento \n Área: {area} \n Perímetro: {perimetro}'
    def local(self, quanti_pisos, tamanho_local):
        self.pisos = quanti_pisos
        self.tam_local = tamanho_local
    
        print(f'A quantidade de pisos necessária para preencher {self.tam_local}m² é de {round(self.pisos)} pisos \n {20 * '='}')

print('Preciso que me informe as informações do local')
comprimento = float(input("Digite o comprimento do local (m): "))
largura = float(input('Digite a largura do local (m): '))
tamanho_local = (comprimento * largura)
print(f'O local tem {tamanho_local} m²')
print()


print('Agora preciso das informações do materia')
com_piso = float(input('Digite o comprimento do piso (cm): '))
lar_piso = float(input("Digite a largura do piso (cm): "))
tamanho_piso = (com_piso * lar_piso) / 100

quantidades_de_pisos = tamanho_local / tamanho_piso


retangulo = Retangulo(comprimento, largura)
print(retangulo.mudar_valores())
retangulo.local(quantidades_de_pisos, tamanho_local)