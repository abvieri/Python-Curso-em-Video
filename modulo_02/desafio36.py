#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual seu salário: '))
anos = int(input('Em quantos anos você planeja pagar? '))

prestacao = casa / (anos*12)
minimo = salario * 0.3

if prestacao > minimo:
    print('Seu empréstimo foi negado')
else:
    print('Seu empréstimo pode ser concedido! A prestação é de R${:.2f}'.format(prestacao))