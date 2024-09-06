class Criptografia:
    def __init__(self, senha):
        self.criptografia = senha
    
    def criptogrando(senha):
        string = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
        criptografada = ''
        posicao = ()
        for i in range(len(senha)):
            if senha[i] != ' ':
                for j in range(senha):
                    for k in range(string):
                        if senha[i] == string[k]:
                            posicao += k
                        else:
                            ...