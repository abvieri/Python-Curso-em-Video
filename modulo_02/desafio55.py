#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No fi
# nal, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for cont in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(cont)))
    if maior == 0 or menor == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

if  menor == maior:
    print('Todos os pesos são iguais!')
else:
    print('O maior peso foi {:.2f}Kg e o menor {:.2f}Kg'.format(maior,menor))