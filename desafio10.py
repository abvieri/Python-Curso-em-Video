#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input('Digite seu dinheiro em reais: '))
dolar = reais / 4.97
print('R${:.2f} convertido em dólares é: ${:.2f}'.format(reais, dolar))