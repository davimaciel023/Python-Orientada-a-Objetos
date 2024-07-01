"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar 
 - número do canal 
 - aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""
class Tv:
    def __init__(self, canal, volume):
        self._canal = canal
        self._volume = volume
    
    def volume_tv(self, volume):
        if volume == '1':
            if self._volume == 100:
                print("Volume está no Máximo")
            else:
                self._volume += 5
                print(f"Volume aumentado para {self._volume}")
        
        elif self._volume == '2':
            if self._volume == 0:
                print("Volume está zerado")
            else:
                self._volume -= 5
                print(f"Volume diminuido para {self._volume}")

    def numero_canal (self, canal):
        print(f'O canal é {self._canal}')

    def fprint(self):
        print('=' * 30)

canal = input('Digite o número do canal: ')
quantidade_volume = int(input("Quantidade do volume: "))
print('Aumentar volume = 1' '\n''Diminuir volume = 2')
volume = input('Qual você escolhe, 1 ou 2? ')
tv = Tv(canal, quantidade_volume)
tv.fprint()
tv.numero_canal(canal)
tv.volume_tv(volume)
tv.fprint()
