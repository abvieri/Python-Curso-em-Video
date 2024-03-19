# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = input('Digite algo: ')
print('É um número: {} '.format(valor.isnumeric()))
print('É alfabético: {}'.format(valor.isalpha()))
print('É alphanumérico: {}'.format(valor.isalnum()))
print('Está em maiúsculas: {}'.format(valor.isupper()))
print('Está em minúsculas: {}'.format(valor.islower()))
print('Está capitalizado: {}'.format(valor.istitle()))
