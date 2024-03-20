#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Nome em Maiusculo: {}'.format(nome.upper()))
print('Nome em Minusculo: {}'.format(nome.lower()))
print('Total de letras: {}'.format(len(nome) - nome.count(' ')))
print('Total de letras do primeiro nome: {}'.format(len(nome.split()[0])))