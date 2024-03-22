#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
num = random.randint(0, 5)
jogador = int(input('Vamos jogar um jogo? Pensei em um número, tente acertar qual é: '))
print('Você venceu :(' if num == jogador else 'Eu ganhei :) o número era {}'.format(num))