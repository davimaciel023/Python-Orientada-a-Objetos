# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Noticacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NoticacaoEmail(Noticacao):
    def enviar(self) -> bool: 
        print('Email: enviando', self.mensagem)
        return True

class NoticacaoSMS(Noticacao):
    def enviar(self) -> bool: 
        print('SMS: enviando', self.mensagem)
        return True

def notificar(notificacao: Noticacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print("Enviado")
    else:
        print('Não enviado')

notificar(NoticacaoEmail('Testando email'))
notificar(NoticacaoSMS('Testando sms'))