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
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    
class Motor:
    def __init__(self, nome):
        self.nome = nome
    
class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

porsche = Carro('Porsche')
zuffenhausen = Fabricante('Zuffenhausen')
motor_9_0 = Motor('9.0')
porsche.fabricante = zuffenhausen
porsche.motor = motor_9_0
print(porsche.nome, porsche.fabricante.nome, porsche.motor.nome)