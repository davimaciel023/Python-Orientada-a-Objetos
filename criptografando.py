def criptografando(senha, casas):
    criptografia = ''
    for i in range(len(senha)):
        if senha[i] != ' ':
            criptografia += strings[i+casas]
        else:
            criptografia += senha[i]
    print(criptografia)

senha = input("Digite uma frase: ").lower()
casas = int(input("Quantas casa quer pular ? "))
strings = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
criptografando(senha, casas)