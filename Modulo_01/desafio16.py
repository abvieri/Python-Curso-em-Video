#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input("Digite um número real: "))
print("O valor digitado foi {}, sua porção inteira é: {}".format(num, int(num)))