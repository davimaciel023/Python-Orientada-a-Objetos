class Criptografia:
    def __init__(self, frase):
        self.criptografia = frase
    
    def criptografando(frase, pular):
        self.string = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", ' ')
        self.criptografada = ''
        posicao = ()
        for i in range(len(frase)):
            if frase[i] != ' ':
                for j in range(len(frase)):
                    for k in range(len(self.string)):
                        if frase[j] == self.string[k]:
                            posicao += k
                        else:
                            ...
                
                for l in range(len(frase)):
                    if (posicao[l] + pular) <= 26:
                        self.criptografada += self.string[posicao[l]]

                    else:
                        self.criptografada += self.string[(26-(posicao[l] - pular))]
            else: 
                ...
            print(self.criptografada)
    
frase = input('Digite uma frase: ').lower()
pular = int(input('Quantas casas que pular? '))

c = Criptografia(frase)
c.criptografando(frase, pular)