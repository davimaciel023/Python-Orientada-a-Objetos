import os
os.system('cls')

while True:
    print('''
____ ____ _    ____ _  _ _    ____ ___  ____ ____ ____ 
|    |__| |    |    |  | |    |__| |  \ |  | |__/ |__| 
|___ |  | |___ |___ |__| |___ |  | |__/ |__| |  \ |  |                                                    

 _____________________
|  _________________  |
| |    calculadora  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |   
|_____________________|

''')
    
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    print('\n 1- Adição \n 2- Subtração \n 3- Multiplicação \n 4- Divisão')
    oper = int(input('Escolha: '))

    if oper == 1:
        soma = numero1 + numero2
        print()
        print(f'A soma deu {soma}')
        print('=' * 20)
    elif oper == 2:
        sub = numero1 - numero2
        print()
        print(f'A subtração deu {sub}')
        print('=' * 20)
    elif oper == 3:
        mult = numero1 * numero2
        print()
        print(f'A multiplicação deu {mult}')
        print('=' * 20)
    elif oper == 4:
        div = numero1 / numero2
        print()
        print(f'A divisão deu {div}')
        print('=' * 20)
    else:
        print('Você não digitou o número certo')
        continue

    conti = input('Mais uma conta? ').lower()
    if conti == 'sim':
        os.system('cls')
        continue
    else: 
        break