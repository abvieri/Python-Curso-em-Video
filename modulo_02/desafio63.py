#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

num = int(input('Digite a quantidade de números que deseja ver: '))
t1 = 0
t2 = 1
cont = 3
total = 0

print('{} -> {}'.format(t1, t2), end='')
while cont <= num:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('\nFim')
