#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + (10-1) * razao
for cont in range(termo, decimo + razao, razao):
    print(cont, end='-> ')
print('Fim')