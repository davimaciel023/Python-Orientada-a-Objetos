# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...
class MyOpen:
    def __init__(self, caminho_arquivo, modo) -> None:
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print("Abrindo arquivo")
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('EXIT')  
        self._arquivo.close()


with MyOpen('aula30.txt', 'w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.write('linha 3\n')
    print('With', arquivo)