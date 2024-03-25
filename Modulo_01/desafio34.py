#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario_base = float(input('Digite o salário base: '))

if salario_base > 1251.00:
    print('Seu novo salário é {}'.format((salario_base*0.10) + salario_base))
else:
    print('Seu novo salário é {}'.format((salario_base*0.15) + salario_base))