#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

import random
mak = random.randint(1, 3)

jogador = int(input('Escolha uma das opções: \n1- Pedra\n2- Papel\n3- tesoura\n'))

if  mak == 1 and jogador == 1 or mak == 2 and jogador ==  2 or mak == 3 and jogador == 3:
    print("EMPATE")
elif mak == 1:
    if jogador == 2:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
elif mak == 2:
    if jogador == 1:
        print('Você perdeu!')
    else:
        print('Você ganhou!')
elif mak == 3:
    if jogador == 1:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
else: 
    print('Opção inválida! Escolha novamente.')