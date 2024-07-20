"""
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.
 Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
"""
class ContaInvestimento:
    def __init__(self, saldo,  taxas_juros):
        self.saldo = saldo
        self.juros = taxas_juros
    
    def adicionarjuros(self, tempo):
        self.tempo = tempo
        montante = (self.saldo * (1 + (self.juros/100))**self.tempo)

        print(f"O valor do montante é: {montante :.2f} reais")

conta = ContaInvestimento(1000, 10)
conta.adicionarjuros(5)