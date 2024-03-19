#Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('digite um número:'))
n2 = int(input('digite outro número:'))
soma = n1 + n2
print('O valor da soma de {} e {} da {}'.format(n1, n2, soma))