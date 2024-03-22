#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade do carro? em KM'))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Voçê está dentro da velocidade permitida.')
else: 
    print('Você foi multado em R${}'.format(multa))