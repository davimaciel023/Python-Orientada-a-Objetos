"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. 
Exemplo de uso:
    meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
    meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
    meuFusca.andar(100);            # anda 100 quilômetros.
    meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
"""
class Carro:
    def __init__(self, consu_combustivel):
        self._consu_combustivel = consu_combustivel

    def adicionar_gasolina(self, gasolina):
        self._gasolina = 0
        self._gasolina = gasolina
        print('Nível de gasolina adicionada')
    
    def andar(self, km):
        self.km = km
        nv_combustivel = self._consu_combustivel

        for i in range(self.km):
            if i == self._consu_combustivel:
                self._gasolina -= 1
                self._consu_combustivel += nv_combustivel
                if self._gasolina == 0:
                    print(f'Você andou {i}km')
                    break
    def obter_gasolina(self):
        if self._gasolina == 0:
            print("Gasolina esgotada")
        else: 
            print(f"Restou no tanque {self._gasolina}L de gasolina")

c = Carro(15)
c.adicionar_gasolina(20)
c.andar(100)
c.obter_gasolina()