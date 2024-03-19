#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tRadAngente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Digite um ângulo qualquer: '))
RadAng = radians(ang)
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(sin(RadAng), cos(RadAng), tan(RadAng)))