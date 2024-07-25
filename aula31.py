from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('aula31.txt', 'w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n', 13)
    arquivo.write('linha 3\n')
    print('With', arquivo)