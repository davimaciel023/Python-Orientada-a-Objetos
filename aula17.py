# Exercício com classes
# 1 - Crie uma classe Carro (Nome) - feito
# 2 - Crie uma classe Motor (Nome) - feito
# 3 - Crie uma classe Fabricante (Nome) - feito
# 4 - Faça a ligação entre Carro tem um Motor - feito
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante - feito
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela - feito
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = []
        self.fabricante = []

    def inserir_dados(self, motor, fabricante):
        self.motor.append(Motor(motor))
        self.fabricante.append(Fabricante(fabricante))

    def checando_nomes_dos_carros(self):
        if self.nome == self.nome:
            print('O nome do carro não pode ser igual ao nome anterior')

    def listar_dados(self):
        print(f'Lista do carro: {self.nome}')
        for mt in self.motor:
            print(f'O MOTOR do {self.nome} é: {mt.nome}')
        
        for fab in self.fabricante:
            print(f'O FABRICANTE do {self.nome} é: {fab.nome}')
        print()



    
class Motor:
    def __init__(self, motor):
        self.nome = motor
    
class Fabricante:
    def __init__(self, fabricante):
        self.nome = fabricante

carro = Carro('Fusca')
carro.inserir_dados('gol', 'davi')
carro.listar_dados()

carro = Carro('Porshe')
carro.inserir_dados('bmw', 'davi')
carro.listar_dados()