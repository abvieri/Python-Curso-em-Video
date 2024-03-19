#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

oposto = float(input('Qual o valor do cateto oposto?'))
adjacente = float(input('Qual o valor do cateto adjacente?'))

print('O valor da Hipotenusa é {:.2f}'.format(hypot(oposto, adjacente)))