#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite o valor do produto: '))
desconto = produto * 0.05
print('Seu novo preço com 5% de desconto é R${}'.format(produto - desconto))