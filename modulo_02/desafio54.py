#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maiores = 0
menores = 0

for cont in range(1,9):
    idade = int(input('Digite o {}° ano de nascimento: '.format(cont)))
    idade = 2024 - idade
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('Temos {} maioires de 18 anos e {} menores'.format(maiores, menores))
