#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

num = random.randint(0, 10)
tentativas = 0
jogador = int(input('Vamos jogar um jogo? Pensei em um número, tente acertar qual é: '))

while jogador != num:
    jogador = int(input('Você errou, tente de novo: '))
    tentativas += 1
print('Você venceu! e precisou de {} tentativas para ganhar'.format(tentativas))