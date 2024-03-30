#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Digite o valor para sacar: '))
n50 = 0
n20 = 0
n10 = 0
n1 = 0

while True:
    if valor >= 50:
        valor -= 50
        n50 += 1
    elif valor >= 20:
        valor -= 20
        n20 += 1
    elif valor >= 10:
        valor -= 10
        n10 += 1
    elif valor >= 1:
        valor -= 1
        n1 += 1
    elif valor == 0:
        break
print('\nO usuário recebeu: ')
print(f'{n50} notas de R$50')
print(f'{n20} notas de R$20')
print(f'{n10} notas de R$10')
print(f'{n1} notas de R$1')