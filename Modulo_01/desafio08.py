#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Digite o valor em metros: '))
print('O valor em centímetros é: {:.0f}cm\nO valor em milímetros é: {:.0f}mm'.format(n1*100,n1*1000))