# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable"
class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome, *args, **kwargs):
        print(nome, 'está chamando', self.phone)

call1 = CallMe('9823948223')
call1('Davi')