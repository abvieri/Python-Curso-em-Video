#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário atual: '))
aumento = salario * 0.15
print('Seu novo salário com 15% de aumento é de R${:.2f}'.format(salario + aumento))