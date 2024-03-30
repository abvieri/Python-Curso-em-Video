#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = 0
caros = 0
menor = -1
barato = ''

while True:
    nome = str(input('\nDigite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto: '))
    cond = str(input('Deseja continuar cadastrando? ')).strip().upper()

    float(total)
    total += preco
    if preco > 1000:
        caros += 1
    if menor == -1:
        menor = preco
    if menor > preco:
        menor = preco
        barato = nome

    if cond[0] == 'N':
        break
print(f'\n{total:.2f} foi o total gasto na compra')
print(f'{caros} produtos custam mais de R$1000')
print(f'{barato} é o produto mais barato custando R${menor:.2f}')