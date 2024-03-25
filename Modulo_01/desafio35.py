#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')