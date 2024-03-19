#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a Largura da parede em metros: '))
altura = float(input('Digite a Altura da parede em metros: '))
area = largura * altura
print('A area da parede é de {}m² use {}L de Tinta para pinta-la'.format(area, area/2))