#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).strip().upper()
print('Na frase temos {} vezes a letra A'.format(frase.count('A')))
print('Sua Primeira aparição é na posição {}'.format(frase.find('A')+1))
print('Sua Última aparição é na posição {}'.format(frase.rfind('A')+1))
