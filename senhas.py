#Gerador de senhas
import random

quanti = input("Quantidade? ")
tamanho = input('Tamanho')
senha = []

def gerando_senha(quanti, tamanho):
    strings = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","&","*")

    for i in range(0, int(quanti)):
        for j in range(0, int(tamanho)):
            senha.append(random.choice(strings))
    
        print(senha)
        print()

gerando_senha(quanti, tamanho)