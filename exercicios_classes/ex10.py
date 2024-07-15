"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""
class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel=None):
        self._tipoCombustivel = tipoCombustivel
        self._valorLitro = valorLitro
        self._quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        if self._tipoCombustivel:
            print(f'Você abasteceu {(valor/self._valorLitro):.2f}L de gasolina {self._tipoCombustivel}')


    def abastecerPorLitro(self, valor):
        if self._tipoCombustivel:
            print(f'Você abasteceu {(valor*self._valorLitro):.2f}Reais de gasolina {self._tipoCombustivel}')
        


    def alterarValor(self, valor):
        self._valorLitro = valor

    def alterarCombustivel(self, combustivel):
        self._tipoCombustivel = combustivel

bc = BombaCombustivel('comum', 3)
bc.alterarValor(3.5)
bc.alterarCombustivel('aditivada')
bc.abastecerPorValor(30)
bc.abastecerPorLitro(3)