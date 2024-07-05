"""
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)
    
    def verBucho(self):
        for i in range(len(self.bucho)):
            print(f'O Macaco {self.nome} tem no seu bucho ({self.bucho[i]})')
    
    def digerir(self):
        comidas_permitidas = ['abacaxi', 'maça', 'laranja']
        for i in range(len(self.bucho)):
            if self.bucho[i] in comidas_permitidas:
                print(f'O {self.nome}, adorou o/a {self.bucho[i]}')
            else:
                print(f'O {self.nome}, não gostou e vomitou o/a {self.bucho[i]}')

# macaco1 = Macaco('Juracé')
# macaco2 = Macaco('Feroz')
# macaco1.comer('abacaxi')
# macaco1.verBucho()
# macaco1.digerir()
# print()
# macaco2.comer("limão")
# macaco2.verBucho()
# macaco2.digerir()

Macaco1 = Macaco('Xita') 
Macaco2 = Macaco('Mamaco') 

Macaco1.comer('abacaxi')
Macaco1.comer('limão')
Macaco1.comer('pera')
Macaco1.verBucho()
Macaco1.digerir()
print('\n')
Macaco2.comer('banana')
Macaco2.comer('laranja')
Macaco2.comer('manga')
Macaco2.comer(Macaco1.nome)
Macaco2.verBucho()
Macaco2.digerir()