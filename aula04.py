# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.filmando} já está filmando')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.filmando} não está filmando')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.filmando} não pode fotografar filmando')
            return
        
        print(f'{self.nome} está fotografando...')

c1 = Camera('canon')
c2 = Camera('sony')
c1.filmar()
c1.parar_filmar()
c1.fotografar()
# print(c1.filmando)
# print(c1.filmando)
