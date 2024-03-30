#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from math import ceil

media = 0
homem = 0
mulheres = 0

for cont in range(1,5):
    nome = str(input('\nDigite o {}° nome: '.format(cont)))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).strip().upper()

    media = media + idade
    if sexo == 'MASCULINO':
        if idade > homem:
            homem = idade
            homem_mais_velho = nome
    if sexo == 'FEMININO':
        if idade < 20:
            mulheres = mulheres + 1
print('\nA média das idades lidas é {}'.format(ceil(media/4)))
print('O Homem mais velho é {}'.format(homem_mais_velho))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(mulheres))