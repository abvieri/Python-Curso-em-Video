#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Digite o número inteiro: '))
    if numero < 0:
        break
    for cont in range(0,11):
        print(f'{numero} x {cont:2} = {numero*cont}')
print('Fim')