#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for cont in range(len(junto)-1, -1 ,-1):
    inverso += junto[cont]

if inverso == junto:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')