#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite o número para converter: '))
base = int(input('Escolha a base de conversão:\n1- Binário\n2- Octal\n3- Hexadecimal\n'))

if base == 1:
   print(bin(num)[2:])
elif base == 2:
   print(oct(num)[2:])
elif base == 3:
   print(hex(num)[2:])
else:
   print('Digite um número válido')