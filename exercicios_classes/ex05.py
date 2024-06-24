"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: 
  1- número da conta, 
  2- nome do correntista 
  3- saldo. 

Os métodos são os seguintes: 
  1- alterarNome 
  2- depósito 
  3- saque 

No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""
class ContaCorrente:
    def __init__(self, num_conta, nome_correntista, saldo):
        self.__num_conta = num_conta
        self.__nome_correntista = nome_correntista
        self.__saldo = saldo
  
    def alterarNome(self, nome):
        self.__nome_correntista = nome
        print(f"Seu nome foi alterado para {self.__nome_correntista}")
    
    def deposito(self, deposito):
        
        print(f'O valor deposiado foi {deposito}')
        print(f'Seu saldo antigo é de {self.__saldo}')
        self.__saldo += deposito
        print(f'Seu saldo atual é de {self.__saldo}')

    def saque(self, valor):
        self.__saldo -= valor
        print(f'O valor sacado foi de {valor}')
        print(f'Seu saldo é de {self.__saldo}')

    def fprint(self):
      print(20 * '=')
        
conta = ContaCorrente(123, 'Davi', 300)
conta.fprint()
conta.alterarNome('Nagilla')
conta.deposito(242)
conta.saque(511)
conta.fprint()