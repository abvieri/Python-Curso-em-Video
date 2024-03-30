#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
from time import sleep

seq= 0
print('Vamos jogar par ou ímpar? ', end='')
while True:
    comp = random.randint(0,10)
    escolha = str(input('Escolha entre Ímpar ou Par: ')).strip().upper()
    sleep(1)
    print('1')
    sleep(1)
    print('2')
    sleep(1)
    print('3')
    sleep(1)
    jogador = int(input('E... Lá. Digite seu número: '))
    resultado = (jogador + comp)%2

    if resultado == 0:
        resultado = str('P')
    else:
        resultado = str('Í')

    if escolha[0] == resultado:
        print(f'Parabéns você ganhou! Eu escolhi {comp}, vamos de novo')
        seq = seq + 1
    else:
        break
print(f'Você perdeu, eu escolhi {comp}\nSua sequência de vitórias foram {seq}')