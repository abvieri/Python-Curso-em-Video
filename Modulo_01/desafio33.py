#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro valor inteiro: '))
num2 = int(input('Digite o segundo valor inteiro: '))
num3 = int(input('Digite o terceiro valor inteiro: '))

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))